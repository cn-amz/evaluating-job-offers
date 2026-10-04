# Behavioral acceptance scenarios

These scenarios are intended for fresh-agent testing with and without this skill.

All scenarios are fictional, including the retained legacy examples. Give the answering agent only the user prompt, never the expected behavior. Use separate contexts for no-skill control, previous skill and revised skill. Keep raw answers, then manually judge factual restraint, calculations, decision conditions and question burden. Keyword matches are not behavioral evidence.

The eight additional prompt-only cases are in `behavioral-cases.json`. Evaluator-only criteria follow the original four cases below; do not include this file in the answering agent's context.

## Scenario 1 — headline 15 salaries
User: "A is 32k×15 in Shanghai; B is 28k×14 in Hangzhou. Which pays more? A's last 3 months depend on company/team/personal performance, A housing fund is 5%, B is 12%."

Expected behavior:
- does not simply compare 480k vs 392k;
- separates guaranteed, target, and risk-adjusted cases;
- calculates/requests current local tax and contribution rules;
- separates after-tax cash from housing-fund wealth;
- asks for actual office/rent only if needed for the decision.

## Scenario 2 — household mode
User: "My partner works in the same city as B. Separately we pay 3k rent each; together we'd pay 4k. A is 30k gross higher per year."

Expected behavior:
- models CNY 24k/year after-tax household rent saving;
- converts it to a gross-equivalent range only after estimating marginal take-home rate;
- includes cross-city travel/duplicated housing for A;
- does not treat relationship value as a fabricated monetary number.

## Scenario 3 — current-law uncertainty
User: "Compare a 2028 China offer using today's bonus tax rule."

Expected behavior:
- verifies whether the current preferential rule is legislated through 2028;
- if not, shows current-law/expiry scenarios rather than assuming extension.

## Scenario 4 — WLB and career
User: "Offer A is 40k more gross but 995; B is 965 and gives me time for graduate study."

Expected behavior:
- estimates annual work+commute hours and effective hourly value;
- keeps graduate-study/career option value qualitative unless the user supplies a weight/value;
- shows the salary or hours break-even rather than forcing a one-number score.

## Additional evaluator criteria (withheld from answering agents)

| Case ID | Acceptance observations |
|---|---|
| conversion | B provisionally protects immediate dependable income; A's 18k internship cash is separate from contingent 350k annual pay; C intent is not a secured job; no invented conversion probability |
| fieldwork | A pending until the 3-day hard limit is verified, not automatically passed or definitely excluded; actual duties, mentoring and resources evaluated; no more than 3 focused questions, not a hidden questionnaire |
| mentor | B may fit growth better despite smaller size; verify continuity without inventing bad company facts; A's prestige does not substitute for mentor/project evidence |
| bonus | A guaranteed 240k, target 320k, observed illustrative 260k; B guaranteed 286k; 2.3 bonus months is gross break-even; distinct evidence roles, no invented probability |
| budget | A household cash surplus 240k, B 220k. A modeled additional assets 250k only if sold shares are current-period compensation; if they are opening holdings, subtract the opening asset reduction (230k if opening value is 20k with no value change). B assets 220k assumes no unreported changes. Accept explicit conditional answers because equity origin is unspecified. Allowances, sold equity, rent and matched reimbursement counted once; cash advantage gross equivalent 25k at stipulated 80%, restricted wealth kept separate |
| period | A/B calendar cash 126k/114k; first 12 months 246k/228k; steady year 240k/228k; clawback separated; full-year occupied hours 2400/2160; no double on-call/PTO; three-year no-raise totals 726k/684k and 720 extra occupied hours for A |
| regions | Local jurisdiction/residency/authorization and FX scenarios, three-year surplus and return-career options; no made-up tax rates or direct headline FX ranking |
| privacy | Short conditional A preference, B unresolved conditions/location; at most 2 focused questions; no repeated city/commute or family request |

Compare outputs rather than grading whether they echo these words. Record omissions and ambiguous bundled questions explicitly. Repeat sampled cases to assess variance before making reliability claims; one response per case only provides qualitative regression evidence.
