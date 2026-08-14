"""Typed solve results and CSV persistence for comparing models/solvers side by side."""

from __future__ import annotations

import csv
from pathlib import Path

from pydantic import BaseModel


class SolveResult(BaseModel):
    model_name: str
    solver: str
    status: str
    termination_condition: str
    objective: float | None
    wall_time_seconds: float


def write_results_csv(results: list[SolveResult], path: str | Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(SolveResult.model_fields))
        writer.writeheader()
        for result in results:
            writer.writerow(result.model_dump())
