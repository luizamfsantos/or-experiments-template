# notebooks

Exploratory Jupyter notebooks. Keep these read-only/throwaway — once an
analysis is worth keeping, move the logic into `src/` (or `scripts/`) with
tests, and leave the notebook as a thin driver over that code.

`.ipynb_checkpoints/` is gitignored; notebook outputs are not stripped
automatically — clear outputs before committing if they're large or contain
run-specific data.
