from pydantic import BaseModel, Field
from typing import List, Optional

class TaskConfig(BaseModel):
    goal: str
    constraints: List[str] = Field(default_factory=list)
    success_criteria: List[str] = Field(default_factory=list)
    output_path: str = "data/output/output.txt"

class LoopConfig(BaseModel):
    cycles: int = 3
    score_threshold: float = 0.8  # early stop if reached
