import pytest
from pages.home_page import HomePage
from pages.registratation_page import RegistrationPage
from utilities.random_data_utils import RandomDataUtil
from playwright.sync_api import expect

# @pytest.mark.sanity
@pytest.mark.regression

def test_user_registration(page):
    home_page = HomePage(page)
    registration_page = RegistrationPage(page)

    home_page.click_my_account()
    home_page.click_register()

    random_data = RandomDataUtil()

    first_name = random_data.get_first_name()
    last_name = random_data.get_last_name()
    email = random_data.get_email()
    password = random_data.get_password()
    phone = random_data.get_phone_number()

    registration_page.textbox_first_name.fill(first_name)
    registration_page.textbox_last_name.fill(last_name)
    registration_page.textbox_email.fill(email)
    registration_page.textbox_telephone.fill(phone)
    registration_page.textbox_password.fill(password)
    registration_page.textbox_confirm_password.fill(password)


    registration_page.set_privacy_policy()
    registration_page.click_continue()

    confirmation_msg = registration_page.get_confirmation_msg()
    expect(confirmation_msg).to_have_text("Your Account Has Been Created!")