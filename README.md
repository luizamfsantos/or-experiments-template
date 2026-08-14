# experiments-template

A bare scaffold for optimization-research group projects, stripped down from
an ECS-LC Benders-decomposition research repo. It keeps the reusable parts —
Pyomo + Gurobi wiring, config loading, conventions, an optional Lean
formal-proofs setup — and drops everything specific to that original
problem.

## Getting started

1. Rename the project in `pyproject.toml`, `configs/default.yaml`, and
   (if using `formal/`) `formal/lakefile.toml`.
2. Fill in the `TODO`s in `CLAUDE.md` with your actual problem statement.
3. Replace `src/solver/example.py` with your real model, following the same
   Pyomo `ConcreteModel` → `SolverFactory("gurobi").solve(...)` pattern.
4. Point `.env` (gitignored) at your Gurobi license — see
   `src/solver/README.md`.
5. If you don't need Lean formal proofs, delete `formal/` and the matching
   `AGENTS.md` bullet.

```bash
uv sync
uv run pytest -q
uv run python -m src.cli.main
```

## What's here

- `src/config/` — YAML config loading via a typed `RunConfig` (pydantic)
- `src/solver/` — minimal Pyomo + Gurobi example, with the "mock the solver
  in tests" convention already wired up
- `src/cli/` — a thin entrypoint tying config + solver together
- `docs/conventions/` — commit format, module headers, function design,
  testing/mocking conventions
- `formal/` — optional Lean 4 / Mathlib scaffold for formalizing paper
  theorems (delete if unused)
- `configs/`, `Makefile` — placeholders for per-experiment configs and clean
  targets as the project grows

## What was intentionally left out

CI, branch protection, and CODEOWNERS were left for you to set up per the
new project's hosting/team setup. Everything else specific to the original
ECS-LC problem (solver core, generation framework, execution/queue layer,
experiment configs, papers workflow, experiment notes) was dropped — add
back only what your new project actually needs.
