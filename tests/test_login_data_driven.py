import time
import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.my_account_page import MyAccountPage
from utilities.data_reader_util import read_json_file, read_csv_file, read_excel_file


cvs_data = read_csv_file("testdata/logindata.csv")
# json_data = read_json_file("testdata/logindata.json")
# excel_data = read_excel_file("testdata/logindata.xlsx")

@pytest.mark.datadriven
@pytest.mark.parametrize("testName, email, password, expected",cvs_data)
def test_login_data_driven(page , testName, email, password, expected):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    my_account_page = MyAccountPage(page)

    home_page.click_my_account()
    home_page.click_login()

    login_page.enter_email(email)
    login_page.enter_password(password)
    login_page.click_loginbutton()
    time.sleep(3)

    if expected== "success":
        expect(my_account_page.get_my_account_page_heading()).to_be_visible(timeout=3000)
    else:
        expect(login_page.login_error()).to_be_visible(timeout=3000)

