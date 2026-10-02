# Calculation model

Use local currency unless comparison requires FX conversion. Preserve separate columns for spendable cash and restricted/illiquid wealth.

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
`taxable_income = gross_cash - deductible_employee_contributions - statutory deductions - eligible personal deductions`

`after_tax_cash = gross_cash - income/payroll_tax - employee_social_contributions - employee_restricted_contributions + tax-free_cash_benefits`

Do not hard-code tax rules in the skill. Research current brackets, caps, deduction rules, and bonus treatment. If future tax policy is unknown, show current-law and conservative scenarios.

## 3. Wealth accrual

`wealth_accrual = after_tax_cash + employer_owned_or_vested_contributions + employee_restricted_contributions + vested_equity_value`

Report employee contributions separately because they reduce current cash but remain the user's asset. Employer contributions are incremental wealth only to the extent they vest/are owned by the user.

## 4. Living and household economics

`annual_spend = housing + utilities + food + transport + commute + relocation_annualized + duplicated_household_costs + cross_city_travel + dependent_costs`

`annual_cash_surplus = after_tax_cash - annual_spend`

**Household mode:**
`household_surplus = Σ(partners' after_tax_cash) - shared_household_costs - duplicated_costs - cross_city_costs`

When an offer enables cohabitation, compare the household delta, not only the candidate's rent.

### Gross-salary equivalent of an after-tax saving
If marginal take-home rate is `m`:
`gross_equivalent = after_tax_saving / m`

Example: saving 24,000 after tax with a 75% marginal take-home rate is economically similar to about 32,000 of additional gross salary.

## 5. Time-adjusted value

`annual_work_hours = weekly_hours × working_weeks + annual_commute_hours + expected_oncall_or_travel_hours`

`effective_hourly_cash = risk_adjusted_after_tax_cash / annual_work_hours`

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

## 7. Break-even analysis

Prefer decision thresholds over fragile rankings:
- "Offer B needs ≥ X bonus payout to beat A financially."
- "A remains ahead if B's rent is > X/month."
- "B is worth it financially only if its weekly hours stay below X."
- "The city premium required to offset duplicated housing is X gross/year."
