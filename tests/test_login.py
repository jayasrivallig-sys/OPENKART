import configparser
import time
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage
from config import Config # holding valid/invalid credentials
from playwright.sync_api import expect
#
@pytest.mark.sanity
@pytest.mark.regression
def test_invalid_user_login(page):
    home_page = HomePage(page)
    login_page = LoginPage(page)

    home_page.click_my_account()
    home_page.click_login()

    login_page.enter_email(Config.invalid_email)
    login_page.enter_password(Config.invalid_password)
    time.sleep(3)
    login_page.click_loginbutton()

    time.sleep(3)

    expect(login_page.text_error_message).to_be_visible(timeout= 3000)



@pytest.mark.sanity
@pytest.mark.regression
def test_valid_user_login(page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    my_account_page = MyAccountPage(page)

    home_page.click_my_account()
    home_page.click_login()

    login_page.enter_email(Config.email)
    login_page.enter_password(Config.password)
    time.sleep(3)
    login_page.click_loginbutton()

    time.sleep(3)

    expect(my_account_page.get_my_account_page_heading()).to_be_visible(timeout=3000)


