import pytest
from pathlib import Path
from config.settings import BASE_URL, DEFAULT_TIMEOUT_MS, HEADLESS
from utilities.screenshot import save_failure_screenshot

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {**browser_context_args, "viewport": {"width": 1440, "height": 1000}}

@pytest.fixture(autouse=True)
def set_default_timeout(page):
    page.set_default_timeout(DEFAULT_TIMEOUT_MS)
    yield

@pytest.fixture
def base_url():
    return BASE_URL

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            try:
                path = save_failure_screenshot(page, item.nodeid)
                # pytest-html recognizes this extra attachment.
                if hasattr(report, "extras"):
                    from pytest_html import extras
                    report.extras.append(extras.image(str(path)))
            except Exception as exc:
                print(f"Could not capture failure screenshot: {exc}")
