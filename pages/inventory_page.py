from playwright.sync_api import Page, expect

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.inventory_items = page.locator(".inventory_item")
        self.sort_select = page.locator("[data-test='product-sort-container']")
        self.cart_link = page.locator(".shopping_cart_link")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def expect_loaded(self):
        expect(self.title).to_have_text("Products")
        expect(self.inventory_items).to_have_count(6)

    def add_first_item(self):
        self.page.locator(".inventory_item").first.locator("button").click()

    def add_item_by_name(self, name: str):
        item = self.page.locator(".inventory_item").filter(has_text=name)
        item.locator("button").click()

    def sort(self, value: str):
        self.sort_select.select_option(value)

    def product_names(self):
        return self.page.locator(".inventory_item_name").all_text_contents()

    def open_cart(self):
        self.cart_link.click()
