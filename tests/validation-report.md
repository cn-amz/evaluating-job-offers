# Validation record — 2026-10-04

This is a qualitative regression record, not a benchmark or a measured success rate. The original version is commit `f9712a91c0bd88b3e25ab3d6bbb00ea450af1bdd`. All prompts and responses below are fictional; no private user's offer, identity or family details were used.

## Method and raw evidence

Eight new prompt-only cases were supplied from [behavioral-cases.json](behavioral-cases.json) to three separate agent contexts: no-skill control, original skill plus its references, and revised skill plus its references. Expectations, other agents' answers and this report were withheld from answering agents. Each arm answered all eight cases in one context; cases were not individually isolated within an arm. The new cases requested no browsing. The original four cases were also compared using the old and revised skills, with current-source lookup permitted. These are one sample per case/arm, with inherited runtime model settings, no controlled seed and no repeated variance estimate. No claim of five-run micro-test reliability is made.

Raw outputs retained without rewriting:

- [No-skill control, eight cases](results/control-responses.md)
- [Original skill, eight cases](results/baseline-responses.md)
- [Revised skill, eight cases](results/revised-responses.md)
- [Original skill, four legacy cases](results/legacy-baseline.md)
- [Revised skill, four legacy cases](results/legacy-revised.md)

The original and no-skill responses were generated before editing the skill. Baseline weakness was question burden: `fieldwork` bundled travel history, duration, standby, deliverables, research share, site share, mentor and resources into two numbered questions; `privacy` similarly bundled multiple independent checks. Both controls also offered a gross equivalent of the combined cash-plus-restricted-asset advantage in `budget`, albeit with a warning. This is a clarity risk, not an arithmetic error. Correct arithmetic and conditional recommendations were already present; do not attribute all good revised answers to the new skill.

## Manual comparison

| Case | Observation in revised response |
|---|---|
| conversion | Separates intent, conversion internship and formal offer; 18k internship cash versus contingent annual pay; favors the dependable option without a made-up conversion probability |
| fieldwork | Unknown travel stays pending; a confirmed limit violation excludes A; asks three focused questions about A travel, B travel and B's first deliverable, leaving lower-priority checks for later |
| mentor | Allows a small firm to win on actual mentor/project/resource evidence; flags business continuity without inventing failure; no brand-only ranking |
| bonus | 240k guarantee / 260k observed illustration / 320k target versus 286k guarantee; 2.3-month break-even; oral assurance does not override written target status |
| budget | 240k versus 220k cash surplus, modeled assets 250k versus 220k with missing-B-assets assumption; no duplicate rent/subsidy/reimbursement/equity; 25k gross equivalent only for cash advantage; explicitly distinguishes current-period equity from disposal of old holdings |
| period | Calendar, first-12-month and steady-year totals correct; 2400 versus 2160 full-year occupied hours; three-year 726k versus 684k gross cash is not called savings; clawback and 720-hour option difference retained |
| regions | Retains local currency, residency, work authorization, three-year surplus, FX and return-career routes without fabricating rates |
| privacy | Reuses location and commute facts, respects family opt-out, asks two bounded checks and states reversal conditions |
| Legacy 1 | Retains guarantee/target and housing-fund asset/cash separation; B's extra months remain unknown; explicit full-year assumptions and focused questions |
| Legacy 2 | Retains 24k household rent saving, 80% marginal take-home break-even, gross equivalent and three-/four-year scenarios without double counting |
| Legacy 3 | Revised answer retrieved an official announcement ending in 2027 and did not assume a 2028 extension; original lookup failed and transparently reported that limitation. Tool availability differs, so this is not evidence the wording alone improved retrieval |
| Legacy 4 | Retains work/commute and discretionary-study-time comparison; does not invent total effective hourly pay without salaries; conditional recommendation |

No critical arithmetic or requirement violation was found in these revised samples. This does not prove behavior across models, repeated runs, other jurisdictions or all possible prompts. The bundled-question improvement needs repeated independent sampling before a reliable effect size can be claimed. Financial figures in fixtures are stipulated examples, not live tax/payroll advice.

An independent document review found an ambiguity in the `budget` fixture: the origin of sold shares was unspecified, while the initial rubric expected 250k additional assets unconditionally. The rubric was corrected to accept conditional answers without changing the prompt or raw outputs. The revised answer already stated the current-period-compensation assumption and the required offset for opening holdings. For example, disposing of opening holdings worth 20k with no value change would make A's modeled asset increase 230k, despite unchanged 240k cash surplus. This distinction was not explicit in the original/control answers. The review found no other substantive preservation, jurisdiction or privacy issue.

## Package, privacy and license checks

- `python tests/test_structure.py` validates required files, UTF-8, frontmatter, original discovery keywords, local links and prompt-only fixture structure. It deliberately does not score behavior.
- `bash tests/test_structure.sh` is the retained keyword/file smoke check, explicitly labeled as structural. On Windows the Git Bash `/usr/bin` directory must be on its process PATH; no dependencies need installing.
- `git diff --check` checks patch whitespace. The existing household example and MIT `LICENSE` are preserved unchanged.
- Changed content and raw responses were reviewed for private conversation details, local account paths, credentials and unrelated files. Cases are invented; only public source URLs are included. Source essays are linked and summarized in original wording, not copied or relicensed. The historical Nowcoder applicant's personal background is not reproduced.
- Current-source access failures and single-sample limitations are disclosed above. There is no pre-existing GitHub Actions workflow; local structural checks are not described as remote CI.
