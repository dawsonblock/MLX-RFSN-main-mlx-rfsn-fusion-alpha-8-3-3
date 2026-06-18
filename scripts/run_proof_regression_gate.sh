#!/usr/bin/env bash
set -euo pipefail

REQUESTED_OUTPUT_DIR=${1:-}
PROFILE=${4:-main10}
BASELINE_DIR=${2:-benchmarks/proof_baselines/$PROFILE}
ITERATIONS=${3:-5}

# Pre-push gate validates generated proof artifacts without mutating tracked files.
# If an explicit output directory is supplied, preserve the manual artifact-refresh workflow.
TMP_PLOT_DIR=$(mktemp -d)
if [[ -n "$REQUESTED_OUTPUT_DIR" ]]; then
  CURRENT_DIR="$REQUESTED_OUTPUT_DIR"
  mkdir -p "$CURRENT_DIR"
  trap 'rm -rf "$TMP_PLOT_DIR"' EXIT
else
  CURRENT_DIR=$(mktemp -d)
  trap 'rm -rf "$CURRENT_DIR" "$TMP_PLOT_DIR"' EXIT
fi

python3 scripts/generate_proof_artifacts.py \
  --profile "$PROFILE" \
  --output-dir "$CURRENT_DIR" \
  --iterations "$ITERATIONS"

python3 scripts/generate_plots.py \
  --input-dir "$CURRENT_DIR" \
  --output-dir "$TMP_PLOT_DIR"

python3 scripts/check_proof_regression.py \
  --profile "$PROFILE" \
  --baseline-dir "$BASELINE_DIR" \
  --current-dir "$CURRENT_DIR" \
  --strict-missing \
  --output-json "$CURRENT_DIR/regression_report.json" \
  --output-md "$CURRENT_DIR/regression_report.md"

echo "Proof regression gate passed: $CURRENT_DIR vs $BASELINE_DIR"
