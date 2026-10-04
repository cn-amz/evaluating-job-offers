# Calculation model

Use local currency unless comparison requires FX conversion. Preserve separate columns for spendable cash and restricted/illiquid wealth.

## 0. Comparable periods and ledger
Declare start/end dates, months, currency and household scope before calculating. Keep joining calendar year, first complete 12 months and steady year in separate rows. Prorate base/bonus eligibility, probation pay and vesting by actual terms; keep sign-on, relocation and clawbacks visible. An annualized run rate is not cash received in a partial year. Show actual cash timing when rent deposits or delayed reimbursements create a liquidity gap.

For every component record whether it is already included in a supplied cash, expense or asset total. Treat supplied totals as authoritative for their stated scope; do not silently add their parts again. Keep restricted wealth separate from spendable cash. For tax-free allowances use either inclusion in gross cash with correct tax treatment OR addition after deductions, never both. A cash housing subsidy included in income does not also reduce rent. Expense reimbursement is either matched inflow/outflow or netted against the matching expense, never counted as salary plus a second saving.

Screen hard constraints and offer status before ranking. Internship income is its own path; show conversion and non-conversion/continued-search scenarios without inventing a probability. Formal offers with unmet conditions remain pending verification.

## 1. Compensation cases

### Guaranteed cash
`guaranteed_cash = guaranteed_base + guaranteed_signon + guaranteed_allowances + other_contractual_cash`

### Target cash
`target_cash = guaranteed_cash + target_bonus + target_commission`

### Risk-adjusted cash
`risk_adjusted_cash = guaranteed_cash + Σ(variable_component × expected_payout_factor)`

Use payout factors only when supported by evidence or show scenario factors (e.g. 0%, 50%, 100%) instead of one invented probability.

### Equity
Annualize only the vesting portion for the analysis year. Separate:
- public liquid RSU value
- private/illiquid equity estimate
- option intrinsic value and exercise cost
- vesting/cliff and forfeiture risk

Never equate a headline grant with year-one cash.

## 2. After-tax cash

For the relevant jurisdiction:
`taxable_income = taxable_cash_components - deductible_employee_contributions - statutory deductions - eligible personal deductions`

This is a conceptual ledger, not a universal tax formula: determine taxable components, allowable deductions, separate bonus/equity treatment and caps under the actual jurisdiction. Tax-free components may be present in gross cash but are not automatically taxable income.

`after_tax_cash = gross_cash - income/payroll_tax - employee_social_contributions - employee_restricted_contributions + tax_free_cash_not_already_in_gross`

If net sold-equity proceeds are outside this cash total, add them once to spendable inflows; if already included, add nothing. Account for withholding once. Do not treat selling pre-existing holdings as new compensation or newly created wealth: record the offsetting asset reduction separately.

Do not hard-code tax rules in the skill. Research current brackets, caps, deduction rules, and bonus treatment. If future tax policy is unknown, show current-law and conservative scenarios.

## 3. Wealth accrual

`wealth_accrual_before_spending = spendable_inflows + newly_owned_employer_contributions + employee_restricted_contributions + net_new_retained_equity_value`

`new_assets_after_spending = cash_surplus + net_new_restricted_or_retained_assets`

These are different measures: before-spending inflows are not savings. `net_new_retained_equity_value` excludes sold shares already included in spendable inflows, deducts applicable unpaid tax/exercise obligations, and tracks disposals of previously held assets. Never add the full vested equity value again when sale proceeds are already in cash. If the starting portfolio/debt or asset changes are missing, label the result modeled employment-related asset accumulation, not total net-worth change. Value changes on existing holdings are a separate scenario.

Report employee contributions separately because they reduce current cash but remain the user's asset. Employer contributions are incremental wealth only to the extent they vest/are owned by the user.

## 4. Living and household economics

`period_spend = housing + utilities + food + transport + relocation + duplicated_household_costs + cross_city_travel + dependent_costs`

Use mutually exclusive categories: commute fares already in transport and rent already in a household budget are not extra costs. Charge one-off relocation to the period paid; show amortized relocation only as a separately labeled comparison, not cash accounting.

`period_cash_surplus = period_spendable_inflows - period_spend`

**Household mode:**
`household_surplus = Σ(partners' period_spendable_inflows) - nonoverlapping_household_costs`

Include shared and duplicated housing, cross-city trips and dependent costs exactly once. Do not subtract these again if a supplied total already includes them. Combine each partner's additional assets once when showing household asset accumulation.

When an offer enables cohabitation, compare the household delta, not only the candidate's rent.

### Gross-salary equivalent of an after-tax saving
If marginal take-home rate is `m`:
`gross_equivalent = after_tax_saving / m`

Example: saving 24,000 after tax with a 75% marginal take-home rate is economically similar to about 32,000 of additional gross salary.

This is a local approximation under a stated marginal rate, not an average tax rate. For large changes or bracket/contribution-cap crossings, solve `take_home(gross + delta) - take_home(gross) = saving` using current local rules. Convert the cash-surplus difference separately from restricted wealth; do not turn all assets into a spendable-salary equivalent.

## 5. Time-adjusted value

`annual_occupied_hours = weekly_work_hours × actual_working_weeks + commute_hours + additional_nonoverlapping_oncall_or_travel_hours`

`effective_hourly_cash = same_period_risk_adjusted_after_tax_cash / same_period_occupied_hours`

If weekly work hours already include active on-call, do not add them again. Avoid overlapping commute/travel hours. Show passive standby restrictions separately, with explicit sensitivity if valuing them as time. Deduct usable leave/public holidays once; if working weeks already exclude them, do not deduct again. Do not divide half-year pay by a full-year denominator. Describe leave usability and time for rest, study, interviewing and caregiving as option value; do not invent a cash price for it.

Use this as a lens, not the sole decision metric. Salary work often has untracked intensity and uneven overtime.

## 6. Career option value

Do not force uncertain career upside into fake currency. Compare qualitatively or with user-selected weights:
- skill scarcity and transferable skills
- access to high-quality projects/data/compute/customers
- manager/team quality
- promotion and ownership scope
- title/role alignment
- brand/resume value
- future employer set and geographic mobility
- layoff/business risk

For robotics/algorithm roles, test the title against actual model, integration, deployment and site duties; mentor review cadence; usable equipment, authorized datasets and compute. Judge both large and small firms using project/team evidence, not scale alone. Weighted scores are optional user-selected aids after hard screening, not objective truths.

## 7. Break-even analysis

Prefer decision thresholds over fragile rankings:
- "Offer B needs ≥ X bonus payout to beat A financially."
- "A remains ahead if B's rent is > X/month."
- "B is worth it financially only if its weekly hours stay below X."
- "The city premium required to offset duplicated housing is X gross/year."

## 8. Multi-year and regional routes
For each year in a 3–4-year horizon show cash inflows, cash costs, individual and household surplus, and restricted assets separately; cumulative surplus is the sum of yearly surplus. Explicitly model one-off payments, vesting cliffs, clawback/exit, non-conversion or unemployment. Do not assume raises, promotions or tax-policy extensions. Discounted present value is optional with a stated rate, distinct from nominal cumulative savings.

For cross-region offers, compute each in local currency under that jurisdiction/year, then apply dated FX and stress ranges. Check work authorization and residency before declaring an option feasible. Overseas interview questions do not imply overseas tax rules apply in China. If current sources cannot be verified, provide a framework/scenarios instead of fabricated take-home figures.
