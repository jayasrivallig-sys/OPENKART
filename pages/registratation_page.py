from playwright.sync_api import Page,expect

class RegistrationPage:
    def __init__(self, page : Page):
        self.page = page
        self.textbox_first_name = self.page.locator("#input-firstname")
        self.textbox_last_name = self.page.locator("#input-lastname")
        self.textbox_email = self.page.get_by_label("E-Mail")
        self.textbox_telephone = self.page.get_by_role("textbox", name="Telephone")
        self.textbox_password = self.page.locator('input[name="password"]')
        self.textbox_confirm_password = self.page.get_by_role("textbox", name="Password Confirm")
        # self.radio_subscribe_newsletter_yes = self.page.get_by_label("Yes")
        # self.radio_subscribe_newsletter_no = self.page.get_by_label("No")
        self.check_policy = self.page.locator('input[name="agree"]')
        self.button_continue = self.page.locator('input[value="Continue"]')
        self.msg_confirmation = page.locator('h1:has-text("Your Account Has Been Created!")')
        #self.msg_error = page.get_by_text("Warning: You must agree to the Privacy Policy!")


    # def set_registration(self, user_data : dict):
    #
    #     user_data = {
    #                 "fname": "John",
    #                 "lname": "Doe",
    #                 "email": "john.doe@example.com",
    #                 "telephone" : "9876543210",
    #                 "password" : "Test@123",
    #                 "confirm_password" : "Test@123"
    #                 }
    #
    #     self.textbox_first_name.fill(user_data["fname"])
    #     self.textbox_last_name.fill(user_data["lname"])
    #     self.textbox_email.fill(user_data["email"])
    #     self.textbox_telephone.fill(user_data["telephone"])
    #     self.textbox_password.fill(user_data["password"])
    #     self.textbox_confirm_password.fill(user_data["password"])
    #     self.radio_subscribe_newsletter_yes.click()
    #     self.check_policy.check()
    #     self.button_continue.click()
    #     return self.msg_confirmation


    def set_first_name(self, fname: str):
        """Enter the user's first name into the 'First Name' field."""
        self.textbox_first_name.fill(fname)

    def set_last_name(self, lname: str):
        """Enter the user's last name into the 'Last Name' field."""
        self.textbox_last_name.fill(lname)

    def set_email(self, email: str):
        """Enter the user's email address."""
        self.textbox_email.fill(email)

    def set_telephone(self, tel: str):
        """Enter the user's telephone number."""
        self.textbox_telephone.fill(tel)

    def set_password(self, pwd: str):
        """Enter the password."""
        self.textbox_password.fill(pwd)

    def set_confirm_password(self, pwd: str):
        """Re-enter the password in the 'Confirm Password' field."""
        self.set_confirm_password.fill(pwd)

    def set_privacy_policy(self):
        """Select the 'Privacy Policy' checkbox."""
        self.check_policy.check()

    def click_continue(self):
        """Click on the 'Continue' button to submit the registration form."""
        self.button_continue.click()

    def get_confirmation_msg(self):
        """
        Return the confirmation message locator.
        This can be used to verify successful registration.
        """
        return self.msg_confirmation

    # ===== Combined Workflow =====

    # def complete_registration(self, user_data: dict):
    #     """
    #     Complete the full registration process using provided user data.
    #
    #     Example:
    #     user_data = {
    #         "firstName": "John",
    #         "lastName": "Doe",
    #         "email": "john.doe@example.com",
    #         "telephone": "9876543210",
    #         "password": "Test@123"
    #     }
    #     """
    #     self.set_first_name(user_data["firstName"])
    #     self.set_last_name(user_data["lastName"])
    #     self.set_email(user_data["email"])
    #     self.set_telephone(user_data["telephone"])
    #     self.set_password(user_data["password"])
    #     self.set_confirm_password(user_data["password"])
    #     self.set_privacy_policy()
    #     self.click_continue()
    #
    #     # Return confirmation message element for validation
    #     return self.msg_confirmation












