# 🧠 SIMP — Self-Improving Multi-Agent Planner

SIMP (Self-Improving Multi-Agent Planner) is an agentic AI system designed to autonomously plan, execute, evaluate, and improve task solutions using a multi-agent architecture.

Unlike traditional AI systems that produce a single-pass response, SIMP introduces an iterative reasoning loop where multiple specialized agents collaborate to generate better outputs over time.

The system implements a Planner → Executor → Evaluator → Reflector workflow that allows the model to analyze its own outputs, generate feedback, and improve its reasoning in subsequent cycles. 

## 🚀 Motivation

Traditional AI planning systems often suffer from:

•lack of transparency in decision-making

•inability to adapt to new goals

•limited capacity to learn from past mistakes

Most systems generate a single plan and execute it without feedback loops.

SIMP addresses this limitation by introducing a modular multi-agent framework that iteratively improves decision quality through reflection and evaluation cycles. 

## 🧠 Core Concept

SIMP uses multiple AI agents that collaborate to solve a task.

Each agent performs a specialized role:

Agent	Role
Planner	Breaks user goals into structured steps
Executor	Executes the planned tasks using LLM reasoning
Evaluator	Scores the output and provides feedback
Reflector	Uses feedback to improve the next cycle

This architecture allows the system to self-correct and improve over time.

🏗 System Architecture
User Input
    │
    ▼
Planner Agent
(Task decomposition)
    │
    ▼
Executor Agent
(Task execution via LLM)
    │
    ▼
Evaluator Agent
(Score + feedback generation)
    │
    ▼
Reflector Agent
(Self-improvement rules)
    │
    ▼
Next Iteration


This loop repeats until the system reaches acceptable output quality.

# ⚙️ Technology Stack

### Core Technologies

•Python

•Large Language Models (LLMs)

### Frameworks & Tools

•LangGraph / Agent orchestration

•Streamlit (frontend interface)

•JSON memory storage

•Python dataclasses

### System Components

•Agent modules

•Orchestrator

•Memory system

•Evaluation engine

# 🧩 Key Components

1️⃣ Planner Agent

The planner converts a high-level user goal into structured steps.

Example:

User Goal:
"Create a literature review table."

Planner Output:
1. Identify relevant papers
2. Extract key findings
3. Summarize results
4. Structure into Markdown table

2️⃣ Executor Agent

The executor performs the planned tasks using an LLM.

Example implementation:

class Executor:
    def __init__(self, llm):
        self.llm = llm

    def execute(self, plan):
        prompt = f"Execute the following plan:\n{plan}"
        return self.llm.generate(prompt)
        
3️⃣ Evaluator Agent

The evaluator analyzes the generated output and assigns:

•numerical score (0–1)

•natural language feedback

It checks:

•correctness

•completeness

•formatting

•alignment with task goals. 


4️⃣ Reflector Agent

The reflector extracts lessons from the evaluator feedback and generates rules for the next cycle.

Example:

Feedback:
Cells too long.

Reflection Rule:
Keep responses under 20 words per cell.

These rules improve the system's reasoning in future iterations.

# 🔁 Self-Improvement Loop
Plan → Execute → Evaluate → Reflect → Improve

Each cycle produces:

•plan

•output

•feedback

•performance score

•reflection rules

All results are stored in memory.json so the system can learn from past cycles. 

# 📊 Evaluation Metrics

System performance is measured using:

Metric	Meaning
Accuracy	Overall correctness of outputs
Precision	Quality of predictions
Recall	Ability to capture important cases
F1 Score	Balance between precision and recall

Because SIMP learns from feedback, these metrics improve across cycles, unlike traditional single-pass LLM systems. 

# 💡 Applications

SIMP can be applied to:

•AI research assistants

•autonomous decision systems

•robotics planning

•compliance auditing

•customer support automation

•knowledge management systems. 

# 📂 Project Structure

simp/

│

├── agents/

│   ├── planner.py

│   ├── executor.py

│   ├── evaluator.py

│   └── reflector.py

│

├── orchestrator/

│   └── orchestrator.py

│

├── memory/

│   └── memory.json

│

├── ui/

│   └── app.py (Streamlit interface)

│

└── config/

# 🔮 Future Improvements

Potential enhancements include:

•persistent long-term agent memory

•reinforcement learning feedback

•distributed multi-agent collaboration

•tool-enabled reasoning (APIs, search)

•autonomous research agents

# 👩‍💻 Author

Suhani Srivastava

B.Tech CSE – Cyber Physical Systems

VIT Chennai
