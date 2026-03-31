import time

import pytest

from pages import registratation_page, search_results_page
from pages.home_page import HomePage
from pages.registratation_page import RegistrationPage
from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage
from pages.logout_page import LogoutPage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from config import Config
from utilities.random_data_utils import RandomDataUtil
from playwright.sync_api import expect
from pages.shopping_cart_page import ShoppingCartPage


@pytest.mark.end_to_end
def test_end_to_end(page):
    # Step 1: Register a new account and capture the generated email
    registered_email, registered_password = perform_registration(page)
    print("Registration completed successfully!")

    # Step 2: Logout after registration
    perform_logout(page)
    print("Logout completed successfully!")

    # Step 3: Login with registered email
    perform_login(page, registered_email, registered_password)
    print("Login completed successfully!")

    # Step 4: Search product and add to cart
    add_product_to_cart(page)
    print("Product added to cart successfully!")

    # Step 5: Verify cart details
    verify_shopping_cart(page)
    print("Shopping cart verification completed!")


def perform_registration(page):
    home_page = HomePage(page)
    registration_page = RegistrationPage(page)

    home_page.click_my_account()
    home_page.click_register()

    # Fill registration form with random data
    random_data = RandomDataUtil()

    first_name = random_data.get_first_name()
    last_name = random_data.get_last_name()
    email = random_data.get_email()
    phone = random_data.get_phone_number()
    password = random_data.get_password()

    registration_page.textbox_first_name.fill(first_name)
    registration_page.textbox_last_name.fill(last_name)
    registration_page.textbox_email.fill(email)
    registration_page.textbox_telephone.fill(phone)
    registration_page.textbox_password.fill(password)
    registration_page.textbox_confirm_password.fill(password)

    registration_page.set_privacy_policy()
    registration_page.click_continue()

    # Validate confirmation message
    confirmation_msg = registration_page.get_confirmation_msg()
    expect(confirmation_msg).to_have_text("Your Account Has Been Created!")

    return email, password


def perform_logout(page):
    my_account = MyAccountPage(page)
    logout_page = LogoutPage(page)

    my_account.click_logout()
    expect(logout_page.get_continue_button()).to_be_visible(timeout=3000)  # checks continue button on logout page

    logout_page.click_continue()  # navigates to HomePage
    expect(page).to_have_title("Your Store")  # Checks Home Page Exists with title


def perform_login(page, email, password):
    home = HomePage(page)
    home.click_my_account()
    home.click_login()

    login = LoginPage(page)
    login.enter_email(email)
    login.enter_password(password)
    login.click_loginbutton()

    my_account_page = MyAccountPage(page)
    # Verify successful login by checking 'My Account' page presence
    expect(my_account_page.get_my_account_page_heading()).to_be_visible(timeout=3000)


# -------------------------------------------------------------
# Helper Function: Search and Add Product to Cart
# -------------------------------------------------------------
def add_product_to_cart(page):
    # search results + add produc to cart

    # Get product name from configuration
    product_name = Config.product_name
    product_quantity = Config.product_quantity

    # Create Page Object instances
    home_page = HomePage(page)
    search_results_page = SearchResultsPage(page)

    #  Enter product name and click Search
    home_page.enter_product_name(product_name)
    home_page.click_search_button()

    # Verify that the search results page is displayed
    expect(search_results_page.get_search_results_page_header()).to_be_visible(timeout=3000)

    # Validate if the searched product appears in results
    expect(search_results_page.is_product_exist(product_name)).to_be_visible(timeout=3000)

    product_page = search_results_page.select_product(product_name)
    product_page.set_quantity(product_quantity)
    product_page.click_add_to_cart()

    # Verify success message appears
    # expect(product_page.alert_confirmation_message_addtocart()).to_be_visible(timeout=3000)


def verify_shopping_cart(page):

    product_page = ProductPage(page)
    product_page.click_to_navigate_to_cart()

    shopping_cart = product_page.click_view_cart_items_popup()

    config = Config()

    print(" Navigated to Shopping Cart Page!")
    time.sleep(1)
    expect(shopping_cart.get_total_price).to_have_text(config.total_price)
