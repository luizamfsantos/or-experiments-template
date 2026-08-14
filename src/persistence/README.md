# `src/persistence`

`results.py` defines `SolveResult` — the common shape every model/solver
comparison should report into (model name, solver, status, termination
condition, objective, wall time) — and `write_results_csv` to dump a list of
them to disk.

Build one `SolveResult` per run regardless of which modeling approach or
solver produced it, so different formulations land in the same table and are
directly comparable. See `experiments/compare_modeling/` for the pattern in
use.
