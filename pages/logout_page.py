from playwright.sync_api import Page, expect
from  pages.home_page import HomePage

class LogoutPage:
    def __init__(self, page :Page):
        self.page = page
        #self.button_logout = page.locator("text='Logout'").nth(1)
        self.button_continue = page.locator(".btn.btn-primary")

    def click_continue(self):
        try:
            self.button_continue.click()
        except Exception as e:
            print(f"error on continue to new login : {e}")
            raise

    def get_continue_button(self):
        try:
            return self.button_continue
        except Exception as e:
            print(f" Exception while fetching 'Continue' button locator: {e}")
            return None



