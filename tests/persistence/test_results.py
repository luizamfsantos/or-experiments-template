"""Tests for the SolveResult schema and CSV persistence."""

from __future__ import annotations

import csv

from src.persistence import SolveResult, write_results_csv


def test_write_results_csv_round_trips(tmp_path):
    results = [
        SolveResult(
            model_name="example",
            solver="gurobi",
            status="ok",
            termination_condition="optimal",
            objective=20.0,
            wall_time_seconds=0.01,
        ),
        SolveResult(
            model_name="example",
            solver="appsi_highs",
            status="ok",
            termination_condition="optimal",
            objective=20.0,
            wall_time_seconds=0.02,
        ),
    ]
    out_path = tmp_path / "results.csv"

    write_results_csv(results, out_path)

    with open(out_path) as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 2
    assert rows[0]["solver"] == "gurobi"
    assert rows[1]["solver"] == "appsi_highs"
