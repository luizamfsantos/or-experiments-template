# compare_modeling

Reference pattern for comparing modeling approaches: run the same problem
through multiple solvers and/or formulations and collect the results into one
comparable table.

```bash
uv run python -m experiments.compare_modeling.run
```

Writes `experiments/compare_modeling/outputs/results.csv` (gitignored) with
one row per `(model, solver)` combination: status, termination condition,
objective, wall time. Add solver names to `SOLVERS_TO_COMPARE` in `run.py`
to compare backends, or add model builders to compare formulations.
