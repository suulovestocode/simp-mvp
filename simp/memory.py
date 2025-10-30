import json, os
from typing import Any, Dict, List

MEM_PATH = os.path.join(os.path.dirname(__file__), "memory.json")

def _load() -> Dict[str, Any]:
    if not os.path.exists(MEM_PATH):
        return {"rules": [], "win_snippets": []}
    with open(MEM_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def _save(mem: Dict[str, Any]) -> None:
    with open(MEM_PATH, "w", encoding="utf-8") as f:
        json.dump(mem, f, indent=2, ensure_ascii=False)

def add_rule(rule: str) -> None:
    mem = _load()
    if rule not in mem["rules"]:
        mem["rules"].append(rule)
    _save(mem)

def add_win_snippet(name: str, text: str) -> None:
    mem = _load()
    mem["win_snippets"].append({"name": name, "text": text})
    _save(mem)

def get_rules() -> List[str]:
    return _load().get("rules", [])

def get_win_snippets() -> List[dict]:
    return _load().get("win_snippets", [])
