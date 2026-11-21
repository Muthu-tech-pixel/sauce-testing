from playwright.sync_api import Page, expect

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.items = page.locator(".cart_item")
        self.checkout_button = page.locator("#checkout")
        self.continue_shopping = page.locator("#continue-shopping")

    def expect_loaded(self):
        expect(self.title).to_have_text("Your Cart")

    def checkout(self):
        self.checkout_button.click()
