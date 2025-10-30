import argparse, json, os
from dotenv import load_dotenv
from simp.config import TaskConfig, LoopConfig
from simp.orchestrator import Orchestrator

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", type=str, default="tasks/sample_litreview.json")
    parser.add_argument("--cycles", type=int, default=3)
    args = parser.parse_args()

    load_dotenv()

    with open(args.task, "r", encoding="utf-8") as f:
        task_dict = json.load(f)
    task = TaskConfig(**task_dict)
    loop = LoopConfig(cycles=args.cycles)

    orch = Orchestrator(task, loop)
    orch.run()

if __name__ == "__main__":
    main()
