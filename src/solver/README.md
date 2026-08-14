# `src/solver`

`example.py` shows the intended pattern for wiring a Pyomo model to Gurobi:
build a `ConcreteModel`, hand it to `pyo.SolverFactory("gurobi").solve(...)`.
Replace it with the real model as the project's problem takes shape.

## Gurobi license

Requires a Gurobi license. Point to it with a `.env` file (gitignored):

```
LICENSE_PATH="/path/to/gurobi.lic"
GUROBI_PATH="/path/to/gurobi-install/"
```

## Testing

**Do not call Gurobi directly in tests.** Mock `pyo.SolverFactory` (or the
`.solve()` call on it) instead of requiring a live license — see
`tests/solver/test_example.py` and `docs/conventions/testing.md`.
