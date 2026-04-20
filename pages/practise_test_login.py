from playwright.sync_api import Page, expect
class PracticeAutomation:
    def __init__self(self, page: Page):
        self.page = page
        self.textbox_username = self.page.get_by_role("textbox", name="Username")
        self.textbox_password = self.page.get_by_role("textbox", name="Password")
        self.button_submit = self.page.get_by_role("button", name = "Submit")
        self.alert_error_message = self.page.locator("#error")

    def navigation(self):
        self.page.goto("https://google.com")

    def enter_username(self,username):
        try:
            self.textbox_username.fill(username)
        except Exception as e:
            print(f"Enter valid username : {e}")
            raise

    def enter_password(self,  passsword):
        try:
            self.textbox_password.fill(passsword)
        except Exception as e:
            print(f"Enter valid password : {e}")
            raise
    def click_submit(self):
        try:
            self.button_submit.click()
        except Exception as e:
            print(f"Click submit button not responding : {e})

    def alert_error_message(self):
        try:
            return self.alert_error_message
        except Exception as e:
            print(f"Alert error : {e}")
            return None




            self.textbox_password.fill(password)

