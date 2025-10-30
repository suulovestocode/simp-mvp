# SIMP (Self-Improving Multi-Agent Project) — Minimal MVP

A tiny, beginner-friendly starter to run a **Planner → Executor → Evaluator → Reflector** loop that
**learns across cycles** using simple JSON memory. No fancy frameworks required.

## What you'll need
- Python 3.10+
- VS Code (already installed by you)
- An OpenAI API key

## 1) Setup (one-time)
```bash
# go to a folder where you keep projects
cd /path/to/your/folder

# copy/download this project and then
cd simp-mvp

# (recommended) create a virtual environment
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# install dependencies
pip install -r requirements.txt

# add your keys: copy .env.example -> .env and fill in OPENAI_API_KEY
cp .env.example .env  # Windows: copy .env.example .env
```

## 2) Run a sample task
```bash
python run.py --task tasks/sample_litreview.json --cycles 3
```
This will:
- Ask the Planner to propose a plan
- Let the Executor produce an output (a simple table draft)
- Have the Evaluator score & critique it
- Have the Reflector store lessons to memory
- Repeat for N cycles, expecting improvements

Outputs land in `data/output/` and logs appear in the terminal.

## 3) Try your own task
Duplicate `tasks/sample_litreview.json` and modify fields:
- `goal`: plain-English objective
- `constraints`: rules to follow
- `success_criteria`: what “good” looks like

## Notes
- This MVP uses **one LLM** behind multiple roles (Planner/Executor/…) so you don't need multiple API keys.
- Reflection writes to `simp/memory.json` — safe to delete if you want a clean slate.

## Troubleshooting
- **Module not found**: ensure you activated the virtualenv before running `python run.py`.
- **Auth error**: check `.env` has a valid `OPENAI_API_KEY`.
- **Network**: you need internet to call the model.
- To lower cost, switch to a cheaper model in `.env` (e.g., `gpt-4o-mini` to `gpt-4o-mini-translate` or other lightweight options you have).

Happy building!
