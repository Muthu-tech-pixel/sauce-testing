import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from test_data.users import USERS

@pytest.mark.ui
@pytest.mark.smoke
def test_standard_user_can_login(page, base_url):
    login = LoginPage(page)
    login.open(base_url)
    login.login(**USERS["standard_user"])
    InventoryPage(page).expect_loaded()

@pytest.mark.ui
@pytest.mark.regression
def test_locked_out_user_cannot_login(page, base_url):
    login = LoginPage(page)
    login.open(base_url)
    login.login(**USERS["locked_out_user"])
    login.assert_error_contains("Sorry, this user has been locked out")

@pytest.mark.ui
@pytest.mark.regression
def test_login_rejects_empty_credentials(page, base_url):
    login = LoginPage(page)
    login.open(base_url)
    login.login("", "")
    login.assert_error_contains("Username is required")

@pytest.mark.ui
@pytest.mark.regression
def test_problem_user_can_reach_inventory(page, base_url):
    login = LoginPage(page)
    login.open(base_url)
    login.login(**USERS["problem_user"])
    expect(page).to_have_url(lambda url: "inventory.html" in url)
