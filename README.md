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
3. Set real owners in `.github/CODEOWNERS` (currently `@TODO-set-owner`),
   then turn on branch protection requiring the `CI / test` check and a
   CODEOWNERS review.
4. Replace `src/solver/mip/example.py` with your real model, following the
   same Pyomo `ConcreteModel` → `SolverFactory(solver_name).solve(...)`
   pattern. Add other solving approaches (CP-SAT, heuristics) as sibling
   families under `src/solver/` — see `src/solver/README.md`.
5. Point `.env` (gitignored) at your Gurobi license — see
   `src/solver/README.md`.
6. If you don't need Lean formal proofs, delete `formal/` and the matching
   `AGENTS.md` bullet.

```bash
uv sync
make install-hooks   # one-time per clone — see "Pre-commit hook" below
uv run pytest -q
uv run python -m src.cli.main
```

## Pre-commit hook

`make install-hooks` (or `scripts/install-hooks.sh`) symlinks
`scripts/hooks/pre-commit` into `.git/hooks/pre-commit`. It runs on staged
Python files before every commit:

- `uv run ruff format --check`
- `uv run ruff check`
- `uv run radon cc -s -n B` — fails the commit if any function is below
  complexity grade A

It's a per-clone setup step (git doesn't version `.git/hooks/`), so run it
again after cloning or creating a new worktree.

## What's here

- `src/config/` — YAML config loading via a typed `RunConfig` (pydantic)
- `src/solver/` — solving approaches as sibling families, each reporting into
  the same `SolveResult` so they're directly comparable: `mip/` (Pyomo +
  Gurobi/HiGHS, with a working example), `cpsat/` and `heuristics/`
  (placeholders — see their READMEs). The "mock the solver in tests"
  convention is already wired up in `mip/`.
- `src/persistence/` — `SolveResult` schema + CSV writer, the common shape
  every solver/formulation comparison reports into
- `src/cli/` — a thin entrypoint tying config + solver together
- `docs/conventions/` — commit format, module headers, function design,
  testing/mocking conventions
- `formal/` — optional Lean 4 / Mathlib scaffold for formalizing paper
  theorems (delete if unused)
- `configs/`, `Makefile` — placeholders for per-experiment configs and clean
  targets as the project grows
- `notebooks/` — exploratory Jupyter notebooks (throwaway; promote real logic
  into `src/`)
- `experiments/` — one subdirectory per experiment (driver script + config);
  run outputs are gitignored, not committed. `compare_modeling/` is a working
  reference: runs the example model across multiple solvers and writes a
  comparison table.
- `.github/workflows/ci.yml` — lint (`ruff`) + test (`pytest --cov=src`) on
  push/PR to `main`
- `.github/CODEOWNERS` — placeholder owners; fill in before enabling branch
  protection

## What was intentionally left out

Branch protection itself is a repo-settings toggle done in GitHub, not a
file — turn it on once CODEOWNERS has real owners. Everything else specific
to the original ECS-LC problem (solver core, generation framework,
execution/queue layer, experiment configs, papers workflow, experiment
notes) was dropped — add back only what your new project actually needs.
