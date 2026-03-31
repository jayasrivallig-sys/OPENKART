from playwright.sync_api import Page,expect

class LoginPage:
    def __init__(self,page : Page):
        self.page = page
        self.textbox_email = self.page.locator("#input-email")
        self.textbox_password = self.page.locator("#input-password")
        self.button_login = self.page.locator("input.btn.btn-primary")
        self.text_error_message = self.page.locator("div.alert.alert-danger.alert-dismissible")
        # self.button_forgot_password = self.page.get_by_text("Forgotten Password".first())

    def enter_email(self,email):
        try:
            self.textbox_email.fill(email)
        except Exception as e:
            print(f"Invalid Email : {e}")
            raise

    def enter_password(self, password):
        try:
            self.textbox_password.fill(password)
        except Exception as e:
            print(f"Invalid Password : {e}")
            raise

    def click_loginbutton(self):
        try:
            self.button_login.click()
        except Exception as e:
            print(f"Login Disabled : {e}")
            raise

    def login_error(self):
        try:
            return self.text_error_message
        except Exception as e:
            print(f"Error message : {e}")
            return None

    # def forgetpassword(self):
    #     try:
    #         self.button_forgot_password.click()
    #     except Exception as e:
    #         print(f"Button not working : {e}")
    #         raise

