---
name: evaluating-job-offers
description: Use when a user is comparing one or more job offers, estimating an offer's real value, or deciding between roles with different compensation, locations, benefits, work hours, commute, household or partner constraints, or career upside.
---

# Evaluating Job Offers

## Overview
Compare **decision-relevant value**, not recruiter headline total compensation. Separate verified facts from assumptions, Guaranteed compensation from contingent upside, spendable cash from restricted wealth, and individual economics from household economics.

## Evidence rules
- **Do not fabricate** compensation, tax, benefit, work-hour, location, or career facts.
- For current tax/social-benefit rules, housing costs, company practices, or historical offer bands, research the relevant **jurisdiction** and date. Label evidence as `Offer`, `Official`, `Employee report`, `Historical`, or `Assumption`.
- Prefer ranges to false precision. When sources conflict, show the conflict and use a conservative base case.
- Ask only for missing information that can materially change the result.

## Analysis flow
1. **Normalize compensation.** Split each offer into Guaranteed, target, and upside cases. Treat performance bonus, equity, sign-on, retention, relocation, pensions, employer matches, housing funds, and other benefits separately.
2. **Build a risk-adjusted case.** Discount uncertain bonus/equity using evidence or explicit scenarios; never silently count headline "N months" as guaranteed.
3. **Estimate after-tax cash and wealth.** Apply current local tax, social insurance/payroll deductions, and employee contributions. Keep employer-funded or restricted assets separate from spendable cash.
4. **Model living costs.** Use comparable housing, utilities, food, transport, relocation, and commute assumptions.
5. **Use Household mode when relevant.** Model shared rent, duplicated housing, partner location, childcare/caregiving, cross-city travel, and combined commute. Savings in after-tax expenses are not equivalent to the same amount of pre-tax salary.
6. **Measure time value.** Estimate weekly hours, commute, PTO, on-call/travel, then show effective hourly compensation or annual discretionary time when useful.
7. **Assess career option value.** Compare role scope, learning, manager/team, promotion path, skill scarcity, brand, future mobility, and downside risk. Keep subjective scores separate from financial calculations.
8. **Run sensitivity.** Show what changes the decision: bonus payout, rent, tax treatment, commute, partner location, hours, equity value, or promotion assumptions.

## Output contract
Return: (1) evidence/assumptions, (2) normalized compensation table, (3) after-tax cash and wealth table, (4) living/Household mode comparison, (5) time/WLB comparison, (6) career option analysis, (7) sensitivity or break-even points, and (8) decision-critical questions for HR/team. Give a recommendation only from the user's stated priorities; otherwise describe the trade-off frontier.

## References
Read `references/input-schema.md` for intake fields, `references/calculation-model.md` for formulas, and `references/evidence-and-research.md` for source quality and freshness rules.
