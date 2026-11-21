from playwright.sync_api import Page, expect

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page

    def fill_customer(self, first: str, last: str, postal: str):
        self.page.locator("#first-name").fill(first)
        self.page.locator("#last-name").fill(last)
        self.page.locator("#postal-code").fill(postal)

    def continue_checkout(self):
        self.page.locator("#continue").click()

    def finish(self):
        self.page.locator("#finish").click()

    def expect_complete(self):
        expect(self.page.locator(".complete-header")).to_have_text("Thank you for your order!")
