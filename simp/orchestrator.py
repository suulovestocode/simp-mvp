from dataclasses import dataclass
from typing import Optional
from rich import print as rprint
from .config import TaskConfig, LoopConfig
from .agents import Planner, Executor, Evaluator, Reflector
from .llm import LLM

@dataclass
class Result:
    output: str
    score: float
    feedback: str

class Orchestrator:
    def __init__(self, task: TaskConfig, loop: LoopConfig):
        self.task = task
        self.loop = loop
        self.llm = LLM()
        self.planner = Planner(self.llm)
        self.executor = Executor(self.llm)
        self.evaluator = Evaluator(self.llm)
        self.reflector = Reflector()

    def run(self) -> Result:
        best = Result(output="", score=0.0, feedback="")
        for i in range(1, self.loop.cycles + 1):
            rprint(f"[bold cyan]\n--- Cycle {i}/{self.loop.cycles} ---[/]")
            steps = self.planner.plan(self.task.goal, self.task.constraints, self.task.success_criteria)
            rprint("[bold]Plan[/]:", steps)
            output = self.executor.execute(self.task.goal, steps)
            rprint("[bold]Draft Output[/]:\n", output[:800], "..." if len(output) > 800 else "")
            score, feedback, rules = self.evaluator.evaluate(self.task.goal, output, self.task.success_criteria)
            rprint(f"[bold]Score[/]: {score:.2f}\n[bold]Feedback[/]:\n{feedback}")
            self.reflector.reflect(feedback, rules, output)
            if score > best.score:
                best = Result(output=output, score=score, feedback=feedback)
            if score >= self.loop.score_threshold:
                rprint("[green]Early stop: score threshold reached.[/]")
                break
        # Save best output
        with open(self.task.output_path, "w", encoding="utf-8") as f:
            f.write(best.output)
        rprint(f"[bold green]Saved best output to[/] {self.task.output_path}")
        return best
