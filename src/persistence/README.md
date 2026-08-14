# `src/persistence`

`results.py` defines `SolveResult` — the common shape every model/solver
comparison should report into (model name, solver, status, termination
condition, objective, wall time) — and `write_results_csv` to dump a list of
them to disk.

Build one `SolveResult` per run regardless of which modeling approach or
solver produced it, so different formulations land in the same table and are
directly comparable. See `experiments/compare_modeling/` for the pattern in
use.

## MLflow (optional)

`mlflow_tracking.py` logs a `SolveResult` as an MLflow run — tags (status,
termination condition, solver), params, metrics (objective, wall time), and
optional artifacts (e.g. a written `results.csv`).

- Install the extra: `uv sync --extra tracking`.
- Call `configure_tracking(tracking_uri=..., experiment_name=...)` once at
  startup, or set `MLFLOW_TRACKING_URI` in the environment — `log_solve_result`
  no-ops silently until tracking is configured, so instrumenting a run doesn't
  require MLflow to be installed or reachable.
- Logging failures are caught and warned, never raised — an unreachable
  tracking server cannot fail a solve or a comparison run.

**Do not hit a real MLflow server in tests** — mock `mlflow` itself, the same
way Gurobi is mocked. See `tests/persistence/test_mlflow_tracking.py`.
