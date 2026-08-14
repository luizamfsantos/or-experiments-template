# experiments

One subdirectory per experiment (script + config), following the pattern:
a driver script that loads a `configs/experiments/<name>/*.yaml` and calls
into `src/`. Keep experiment-specific glue here; keep reusable logic in
`src/`.

Run artifacts belong under `<experiment>/outputs/` or `<experiment>/results/`
— both are gitignored — not committed alongside the driver script.
