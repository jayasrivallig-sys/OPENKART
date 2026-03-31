from playwright.sync_api import Page, expect
from pages.shopping_cart_page import ShoppingCartPage

class ProductPage:
    def __init__(self, page : Page):
        self.page =page
        self.textbox_quantity = self.page.locator("input[name='quantity']")
        self.button_add_to_cart = self.page.locator("#button-cart")
        self.button_items_cart = self.page.locator("#cart-total")
        self.alert_confirm_message = self.page.locator(".alert.alert-success.alert-dismissible")
        self.link_view_cart = self.page.locator('strong:has-text("View Cart")')

    def set_quantity(self, qty):
        try:
            self.textbox_quantity.fill('')
            self.textbox_quantity.fill(qty)
        except Exception as e:
            print(f"Quantity not entered : {e}")
            raise

    def click_add_to_cart(self):
        try:
            self.button_add_to_cart.click()
        except Exception as e:
            print(f"Error on clicking addtocart : {e}")
            raise

    # def alert_confirmation_message_addtocart(self):
    #     try:
    #         return self.alert_confirm_message
    #     except Exception as e:
    #         print(f"Error while Items been added to cart : {e}")
    #         return None

    def click_to_navigate_to_cart(self):
        try:
            self.button_items_cart.click()
        except Exception as e:
            print(f"Error while clicking items in Cart : {e}")
            return None

    def click_view_cart_items_popup(self):
        try:
            self.link_view_cart.click()
            return ShoppingCartPage(self.page)
        except Exception as e:
            print(f"Error while clicking 'View cart' : {e}")
            raise
