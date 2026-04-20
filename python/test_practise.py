from pages.practise_test_login import PracticeAutomation
import pytest
from playwright.sync_api import expect

def test_login_practise(page):

    login_page = PracticeAutomation(page)
    login_page.navigation()
    login_page.enter_username("jaya")\
    login_page.enter_password("abc123#")
    expect(login_page).to_have_url("https://google.com")