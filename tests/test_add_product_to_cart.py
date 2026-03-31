import time

import pytest
from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from config import Config

@pytest.mark.sanity
# @pytest.mark.regression
def test_add_product_to_cart(page):

    product_name = Config.product_name
    product_quantity = Config.product_quantity

    home_page = HomePage(page)
    search_results_page = SearchResultsPage(page)

    home_page.enter_product_name(product_name)
    home_page.click_search_button()
    time.sleep(2)
    product_page = search_results_page.select_product(product_name)
    product_page.set_quantity(product_quantity)
    product_page.click_add_to_cart()
    time.sleep(2)

    expect(product_page.alert_confirmation_message_addtocart()).to_be_visible(timeout=4000)