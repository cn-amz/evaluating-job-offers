# Evaluating Job Offers

English | [简体中文](./README.zh-CN.md)

A portable `SKILL.md` for comparing job offers by **real decision value**, not headline total compensation.

It adds several dimensions that many offer-comparison frameworks treat lightly: jurisdiction-aware after-tax cash, guaranteed vs variable pay, employee/employer contributions, cost of living near the actual office, time-adjusted compensation, evidence confidence, and **Household mode** for partners/families whose housing and commute economics change with location.

The primary route is **mainland China campus technical hiring**, including robotics/algorithm roles; other jurisdictions remain supported using local rules and dates. The five lenses remain cash/assets, living costs, time, growth and family. Compare multi-year individual/household surplus, gross-salary equivalents of after-tax savings, and leave/time options as well as annual compensation.

## Decision workflow
- Screen hard constraints before scoring; distinguish intent, conversion internship, conditional offer and formal employment. Unknown feasibility stays pending.
- Reuse known facts and ask at most 1–3 decision-changing questions per turn, fewer if requested. Household details are optional; use totals/ranges and respect declined questions.
- Verify actual algorithm/research, integration, deployment and site duties, mentor time, equipment, data and compute. Company scale and job titles do not prove growth quality.
- Keep joining calendar year, first complete 12 months and steady year separate. Reconcile included subsidies, reimbursements, sold shares and on-call hours once.
- Match evidence to the question and give a conditional recommendation with reversal conditions; never treat historical salaries or an author's preference as current facts.

## Install
Copy the repository contents into `evaluating-job-offers/` in your client's skills directory. Keep `SKILL.md`, all three `references/`, `examples/` and `LICENSE` together; `SKILL.md` alone is discoverable but lacks the full workflow. Do not overwrite a different local version without comparing it first.

For Codex, use its installed skill-installer helper with `--repo cn-amz/evaluating-job-offers --path . --name evaluating-job-offers --ref <reviewed-commit>`. Default destination: `~/.codex/skills/evaluating-job-offers` (or `$CODEX_HOME/skills/evaluating-job-offers`). The helper refuses an existing destination; the skill becomes available on the next turn. No extra runtime dependencies are required.

## Verification
Run `python tests/test_structure.py` on Windows or other platforms; `bash tests/test_structure.sh` retains the original smoke check. These verify packaging/content structure, **not model behavior**. See [tests/scenarios.md](tests/scenarios.md) and [tests/behavioral-cases.json](tests/behavioral-cases.json) for fictional acceptance cases. Run unprimed controls and skill-assisted responses in separate contexts, withhold expectations from the answering agent, and retain raw answers for manual scoring. Single samples do not establish statistical reliability. See [tests/validation-report.md](tests/validation-report.md) for this revision's evidence and limits.

## Example prompts
- "Compare these three offers after tax and living costs."
- "This offer says 15 salaries, but 3 months are performance bonus. What's the real value?"
- "My partner works in another district; compare living together versus two apartments."
- "Which offer gives the best effective hourly pay and three-year career options?"
- "What salary premium would make the farther city break even?"

## Design goals
- Evidence-labeled and date-aware.
- Jurisdiction-agnostic: research current local rules rather than hard-coding one country's tax system.
- Range/scenario based when bonus, equity, WLB, or rent is uncertain.
- Separates spendable cash, restricted wealth, and career option value.
- Supports household economics without assuming that money is the user's only priority.

## Related open-source work reviewed
This skill was designed after reviewing existing public offer-comparison work, including:
- Paramchoudhary/ResumeSkills — `offer-comparison-analyzer`
  https://github.com/Paramchoudhary/ResumeSkills/tree/main/.agents/skills/offer-comparison-analyzer
- yanliudesign/offer-toolkit-skill — `offer-compare-skill`
  https://github.com/yanliudesign/offer-toolkit-skill

Those projects already cover total compensation, non-monetary factors, multi-year growth/risk, and negotiation-adjacent workflows. This project focuses specifically on the **after-tax + statutory benefits + real living cost + time + household** layer and on making uncertainty/evidence provenance explicit.

## License
MIT. See `LICENSE`. Additional reading and source-specific reuse limits are in [references/evidence-and-research.md](references/evidence-and-research.md): 阿秀's offer essay, the historical Nowcoder algorithm-campus retrospective, and general reverse-interview prompts. External author conclusions remain opinions; linked material is not relicensed by this repository.
