
from pages.home_page import HomePage
from playwright.sync_api import expect
import time
from config import Config
from pages.search_results_page import SearchResultsPage
import pytest


@pytest.mark.sanity
def test_search_product_page(page):
    product_name = Config.product_name

    home_page = HomePage(page)
    search_results_page = SearchResultsPage(page)

    home_page.enter_product_name(product_name)
    home_page.click_search_button()

    expect(search_results_page.get_search_results_page_header()).to_be_visible(timeout=2000)
    time.sleep(1)
    expect(search_results_page.is_product_exist(product_name)) .to_be_visible(timeout=2000)
    time.sleep(3)