import time
import pytest
from pages.logout_page import LogoutPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage
from playwright.sync_api import expect
from config import Config

@pytest.mark.regression
def test_user_logout(page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    my_accounts_page = MyAccountPage(page)

    home_page.click_my_account()
    home_page.click_login()

    login_page.enter_email(Config.email)
    login_page.enter_password(Config.password)
    login_page.click_loginbutton()

    expect(my_accounts_page.get_my_account_page_heading()).to_be_visible(timeout=1000)

    logout_page = my_accounts_page.click_logout()

    expect(logout_page.get_continue_button()).to_be_visible(timeout=1500)

    logout_page.click_continue()

    expect(page).to_have_title("Your Store", timeout=1500)
    time.sleep(1)
