.PHONY: install-hooks clean-all

# One-time per-clone setup — see AGENTS.md.
install-hooks:
	@scripts/install-hooks.sh

# Add one `clean-<experiment>` target per experiment as they're added, e.g.:
#   clean-my-experiment:
#   	rm -rf data/generated/my_experiment results/my_experiment
# then list it under clean-all.

clean-all:
	@echo "No experiments registered yet — add clean-<experiment> targets as you add experiments."
