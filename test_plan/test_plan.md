# Test Plan — SauceDemo

## Objective
Assess the core shopping workflow on https://www.saucedemo.com/ including authentication,
inventory display, sorting, cart management and checkout.

## Scope
- Login and logout; positive and negative authentication paths
- Product list and product details
- Sorting by name and price in both directions
- Add/remove products and cart consistency
- Checkout validation, overview, completion and browser navigation
- UI responsiveness and seeded-user exploratory behavior

## Test approach
Use manual exploratory testing for all seeded users and repeatable Playwright/Pytest
checks for critical paths. Validate both visible behavior and browser navigation.
Capture screenshots, timestamps and environment details for defects.

## Test data
All SauceDemo seeded accounts use password `secret_sauce`:
`standard_user`, `locked_out_user`, `problem_user`, `performance_glitch_user`.
Use synthetic checkout details such as Test User / 600001.

## Entry criteria
Target site is reachable; browser and test dependencies are installed; test accounts
are available.

## Exit criteria
All planned cases have a recorded result; critical workflows pass or have documented
defects; each defect has reproducible steps and evidence.

## Risks and assumptions
The public demo site may change without notice. Seeded accounts intentionally exhibit
different behaviors. A behavior designed into a seeded account is not automatically
a defect. Network latency can affect timing observations.

## Deliverables
Test case spreadsheet, automated UI/API tests, HTML report, screenshots, and verified
bug reports with linked GitHub Issues.
