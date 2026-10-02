# Evaluating Job Offers

English | [简体中文](./README.zh-CN.md)

A portable `SKILL.md` for comparing job offers by **real decision value**, not headline total compensation.

It adds several dimensions that many offer-comparison frameworks treat lightly: jurisdiction-aware after-tax cash, guaranteed vs variable pay, employee/employer contributions, cost of living near the actual office, time-adjusted compensation, evidence confidence, and **Household mode** for partners/families whose housing and commute economics change with location.

## Install
Copy the `evaluating-job-offers/` directory into the skills directory used by your agent client. The only required file is `SKILL.md`; keep `references/` and `examples/` for the full workflow.

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
MIT. See `LICENSE`.
