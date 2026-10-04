#!/usr/bin/env bash
set -euo pipefail
# Packaging/keyword smoke checks only; this does not exercise agent behavior.
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
for f in SKILL.md README.md LICENSE references/calculation-model.md references/evidence-and-research.md references/input-schema.md examples/china-household-example.md; do
  test -f "$ROOT/$f"
done
grep -Fq 'name: evaluating-job-offers' "$ROOT/SKILL.md"
grep -Fq 'Household mode' "$ROOT/SKILL.md"
grep -Fq 'risk-adjusted' "$ROOT/SKILL.md"
grep -Fq 'after-tax' "$ROOT/SKILL.md"
grep -Fq 'effective hourly' "$ROOT/SKILL.md"
grep -Fq 'Do not fabricate' "$ROOT/SKILL.md"
