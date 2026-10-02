# Input schema

Collect only fields that can change the decision. Unknown fields remain unknown; do not invent them.

## Offer fields
- company, role, level, employment type
- office location(s), remote/hybrid policy, expected start date
- monthly/annual base salary and currency
- fixed salary months or guaranteed annual base
- target/max bonus; whether contractual; historical payout if known
- sign-on / relocation / retention bonus and clawback terms
- equity type, grant size, vesting schedule, liquidity, current valuation/price, refresh policy
- overtime pay, commission, allowances, meal/transport/housing subsidies
- probation salary differences
- pension/retirement match, provident/housing fund, employer social contributions, insurance premiums
- PTO, sick leave, public holidays, on-call/travel expectations
- expected weekly hours and commute

## Personal/household fields
- tax residency and work jurisdiction
- housing preference: shared room / one-bedroom / family housing / owned home
- likely rent near office and acceptable commute
- partner/family location and whether cohabitation changes housing costs
- duplicated housing or cross-city travel costs
- childcare/caregiving or dependent costs when relevant
- user's priorities: cash, savings, time, city, relationship/family, role fit, learning, stability, prestige, upside
- time horizon: year 1, steady state, 3–4 years

## Confidence fields
For every important input record:
- value
- source: Offer / Official / Employee report / Historical / Assumption
- date
- confidence: high / medium / low

If the user supplies a signed offer or recruiter-written terms, treat those specific terms as higher confidence than public anecdotes, while still separating contractual guarantees from target/variable amounts.
