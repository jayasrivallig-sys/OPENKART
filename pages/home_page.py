from playwright.sync_api import Page, expect


class HomePage:
    def __init__(self, page : Page):
        self.page = page
        self.link_my_account = self.page.locator('span:has-text("My Account")')
        self.textbox_search = self.page.locator('input[placeholder="Search"]')
        self.button_search = self.page.locator('#search button[type="button"]')
        # self.page.link_checkout = self.page.locator(('page.get_by_text("Checkout")'))
        self.link_register = self.page.locator('a:has-text("Register")')
        self.link_login = self.page.locator('a:has-text("Login")')


    def get_home_page_title(self):
        title = self.page.title()
        return title

    def click_my_account(self):
        try:
            self.link_my_account.click()
        except Exception as e:
            print(f"Exception while clicking My account, {e}")

    def click_register(self):
        try:
            self.link_register.click()
        except Exception as e:
            print(f" Registration exception : {e}")

    def click_login(self):
        try:
            self.link_login.click()
        except Exception as e:
            print(f" Exception while clicking 'Login': {e}")
            raise

    def enter_product_name(self,product_name):
        try:
            self.textbox_search.fill(product_name)
        except Exception as e:
            print(f" Exception while entering product name '{product_name}': {e}")
            raise

    def click_search_button(self):
        try:
            self.button_search.click()
        except Exception as e:
            print(f" Exception while clicking 'Search' button: {e}")
            raise
