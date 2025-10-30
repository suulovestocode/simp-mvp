from typing import List, Tuple
from .llm import LLM
from .memory import get_rules, add_rule, add_win_snippet

class Planner:
    def __init__(self, llm: LLM):
        self.llm = llm

    def plan(self, goal: str, constraints: List[str], success_criteria: List[str]) -> List[str]:
        rules = get_rules()
        sys = "You are a careful project planner who outputs numbered step plans."
        user = f"""Goal: {goal}
Constraints: {constraints}
Success criteria: {success_criteria}
Known rules to apply: {rules}

Return 5-8 short, numbered steps. Avoid vague language."""
        out = self.llm.chat(system=sys, user=user)
        steps = [line.strip() for line in out.splitlines() if line.strip()]
        return steps

class Executor:
    def __init__(self, llm: LLM):
        self.llm = llm

    def execute(self, goal: str, steps: List[str]) -> str:
        sys = "You are a precise executor who follows steps exactly and produces concrete output."
        user = f"""Goal: {goal}
Steps to execute:
{chr(10).join(steps)}

Produce the final deliverable only (no commentary). If the goal implies a table, output it in Markdown."""
        return self.llm.chat(system=sys, user=user)

class Evaluator:
    def __init__(self, llm: LLM):
        self.llm = llm

    def evaluate(self, goal: str, output: str, success_criteria: List[str]) -> Tuple[float, str, List[str]]:
        sys = "You are a strict evaluator. You score 0.0-1.0 and give actionable feedback."
        user = f"""Goal: {goal}
Output:
{output}

Success criteria: {success_criteria}

1) Give a single numeric score (0.0-1.0).
2) Then 2-4 bullet points of concrete feedback.
3) Then propose 1-2 short rules we should remember next time (imperative, testable)."""
        resp = self.llm.chat(system=sys, user=user)
        # naive parsing (simple & robust)
        lines = [l.strip() for l in resp.splitlines() if l.strip()]
        score = 0.0
        feedback = []
        rules = []
        for l in lines:
            if score == 0.0:
                # first number found becomes score
                import re
                m = re.search(r"([01](?:\.\d+)?)", l)
                if m:
                    try:
                        score = float(m.group(1))
                        continue
                    except:
                        pass
            if l.startswith(("-", "*")):
                feedback.append(l.lstrip("-* ").strip())
            if l.lower().startswith(("rule:", "remember:", "next time:")):
                rules.append(l.split(":",1)[-1].strip())
        # also collect any lines with strong imperative verbs as rules
        for l in lines:
            if any(l.lower().startswith(k) for k in ["always", "ensure", "verify", "must"]):
                rules.append(l)
        return min(max(score, 0.0), 1.0), "\n".join(feedback), list(dict.fromkeys(rules))  # dedupe

class Reflector:
    def reflect(self, feedback: str, rules: List[str], output: str) -> None:
        # Save rules and a success snippet if score was high (handled by orchestrator).
        for r in rules:
            if r:
                add_rule(r)
        if len(output) > 40:
            add_win_snippet("recent_output", output[:1000])
