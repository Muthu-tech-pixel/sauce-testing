import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from test_data.users import USERS

def login_as_standard(page, base_url):
    LoginPage(page).open(base_url)
    LoginPage(page).login(**USERS["standard_user"])
    InventoryPage(page).expect_loaded()

@pytest.mark.ui
@pytest.mark.smoke
def test_products_sort_a_to_z(page, base_url):
    login_as_standard(page, base_url)
    inventory = InventoryPage(page)
    inventory.sort("az")
    names = inventory.product_names()
    assert names == sorted(names)

@pytest.mark.ui
def test_products_sort_price_low_to_high(page, base_url):
    login_as_standard(page, base_url)
    inventory = InventoryPage(page)
    inventory.sort("lohi")
    prices = [float(x.replace("$", "")) for x in page.locator(".inventory_item_price").all_text_contents()]
    assert prices == sorted(prices)

@pytest.mark.ui
@pytest.mark.smoke
def test_add_product_and_verify_cart_badge(page, base_url):
    login_as_standard(page, base_url)
    InventoryPage(page).add_first_item()
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")

@pytest.mark.ui
def test_remove_product_from_cart(page, base_url):
    login_as_standard(page, base_url)
    inventory = InventoryPage(page)
    inventory.add_first_item()
    inventory.open_cart()
    CartPage(page).expect_loaded()
    page.locator(".cart_item button").click()
    expect(page.locator(".cart_item")).to_have_count(0)

@pytest.mark.ui
@pytest.mark.smoke
def test_complete_checkout_flow(page, base_url):
    login_as_standard(page, base_url)
    InventoryPage(page).add_first_item()
    InventoryPage(page).open_cart()
    cart = CartPage(page)
    cart.expect_loaded()
    cart.checkout()
    checkout = CheckoutPage(page)
    checkout.fill_customer("Test", "User", "600001")
    checkout.continue_checkout()
    expect(page.locator(".title")).to_have_text("Checkout: Overview")
    checkout.finish()
    checkout.expect_complete()

@pytest.mark.ui
def test_checkout_requires_first_name(page, base_url):
    login_as_standard(page, base_url)
    InventoryPage(page).add_first_item()
    InventoryPage(page).open_cart()
    CartPage(page).checkout()
    CheckoutPage(page).fill_customer("", "User", "600001")
    CheckoutPage(page).continue_checkout()
    expect(page.locator("[data-test='error']")).to_contain_text("First Name is required")
