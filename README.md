# Junior QA — Python + Playwright + Pytest

A beginner-friendly end-to-end QA assessment project for SauceDemo UI testing and
ReqRes API testing. It includes a manual test plan, 30+ test cases in Excel/CSV,
Page Object Model classes, reusable fixtures, failure screenshots, HTML reporting,
and GitHub Actions CI.

## Project contents

- `tests/` — SauceDemo UI tests (login, products, sorting, cart, checkout)
- `pages/` — Page Object Model classes
- `test_data/` — seeded SauceDemo user credentials
- `utilities/` — reusable screenshot helper
- `api_tests/` — ReqRes GET, POST, invalid/missing-data and 404 tests
- `config/` — environment-driven settings
- `test_plan/` — test plan and Excel test cases
- `bug_reports/` — professional report template and evidence instructions
- `screenshots/` — automatic failure screenshots
- `reports/` — pytest-html report output
- `.github/workflows/` — CI workflow

## Requirements

- Python 3.10 or newer
- Internet access to SauceDemo and ReqRes
- Chromium browser (installed by Playwright)

## Installation

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

python -m pip install --upgrade pip
pip install -r requirements.txt
playwright install chromium
```

Copy `.env.example` to `.env` if you want to override defaults. `HEADLESS=true` is
the default. Set `HEADLESS=false` to watch the browser.

## Run everything

```bash
pytest
```

The command runs UI and API tests and writes `reports/pytest-report.html`.
To run only UI or API tests:

```bash
pytest tests/ -m ui
pytest api_tests/ -m api
```

Open the HTML report in a browser after the run. Screenshots for failed UI tests
are written to `screenshots/` and linked in the HTML report when supported.

## Test coverage

The UI suite includes:
1. Standard user successful login
2. Locked-out user login rejection
3. Empty credential validation
4. Problem user login smoke check (exploratory behavior should be investigated)
5. Product sorting A–Z
6. Price sorting low-to-high
7. Add product and cart badge
8. Remove product from cart
9. Complete checkout
10. Required first-name validation

The API suite validates:
- GET `/users/2`: status and response schema
- POST `/users`: created response and required response fields
- POST `/users` with empty JSON: accepts documented demo API outcomes and checks body shape
- GET `/users/999999`: 404 and empty JSON response

ReqRes may change behavior or require an API key. The suite sends the public demo
key `reqres-free-v1` by default. If the service changes its authentication policy,
set `REQRES_API_KEY` in your environment to a valid key.

## Framework architecture

Tests call page methods rather than repeating selectors. `conftest.py` provides
Playwright fixtures and a pytest hook that captures screenshots after failed tests.
Configuration is centralized in `config/settings.py`; credentials are centralized
in `test_data/users.py`.

## Bug-hunting instructions (important)

The four seeded accounts are deliberately different:
- `standard_user`
- `locked_out_user`
- `problem_user`
- `performance_glitch_user`

A locked-out login message is expected behavior, not a defect. A slow response from
the performance-glitch account is not automatically a bug. Investigate visible
behavior, compare it with the standard account, reproduce each issue, and save
screenshots before reporting. No bugs or screenshots are pre-claimed in this
starter deliverable because defects must be verified through actual execution.

For each confirmed defect:
1. Duplicate `bug_reports/BUG_REPORT_TEMPLATE.md`.
2. Add exact reproduction steps, expected/actual behavior and evidence.
3. Create a GitHub Issue and attach the screenshot.
4. Add the issue to a GitHub Project board with To Do / In Progress / Done columns.

## Manual test cases

Open `test_plan/test_cases.xlsx` in Excel or LibreOffice. A CSV copy is also supplied.
The test plan is in `test_plan/test_plan.md`.

## CI / GitHub

Push this folder to a GitHub repository. The workflow runs on each push and pull
request and uploads the HTML report and screenshots as a downloadable Actions artifact.
GitHub Issues and the Project board must be created in your repository by you; no
GitHub credentials are included in this ZIP.

## Notes

- UI tests target the live public SauceDemo site and therefore depend on network
  availability and the site's current behavior.
- ReqRes is a public demo API; API contract/authentication can change.
- The HTML report is generated on every pytest run. A failed test does not prevent
  the report from being written.
