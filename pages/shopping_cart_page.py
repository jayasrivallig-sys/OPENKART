from playwright.sync_api import Page, expect
from pages.checkout_page import CheckoutPage

class ShoppingCartPage:
    def __init__(self, page : Page):
        self.page = page
        self.get_total_price = self.page.locator("page.locator("//tr//td.last())""
        self.button_checkout = self.page.locator("a.btn.btn-primary")

    def total_price_of_cart_items(self):
        try:
            return self.get_total_price
        except Exception as e:
            print(f"TotalPrice of items not displayed : {e}")
            return None

    def click_on_checkout(self):
        try:
            self.button_checkout.click()
            return CheckoutPage()
        except Exception as e:
            print(f"Checkout button not working : {e}")
            raise e

    def is_page_loaded(self):
        try:
            return self.button_checkout
        except Exception as e:
            print(f"Checkout button is not enabled : {e}")
            return None