# Behavioral acceptance scenarios

These scenarios are intended for fresh-agent testing with and without this skill.

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
