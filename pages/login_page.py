from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error = page.locator("[data-test='error']")

    def open(self, base_url: str):
        self.page.goto(base_url, wait_until="domcontentloaded")

    def login(self, username: str, password: str):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

    def assert_error_contains(self, message: str):
        expect(self.error).to_contain_text(message)
