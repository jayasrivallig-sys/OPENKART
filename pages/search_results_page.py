from playwright.sync_api import Page, expect
from pages.product_page import ProductPage

class SearchResultsPage:
    def __init__(self, page : Page):
        self.page = page
        self.search_page_header = self.page.locator("#content h1", has_text="Search -")
        self.search_products = self.page.locator('h4 > a')


    def get_search_results_page_header(self):
        try:
            return self.search_page_header
        except Exception as e:
            print(f"Error fetching search results page header: {e}")
            return None

    def is_product_exist(self, product_name):
        try:
            count = self.search_products.count() #count items and store in count
            for i in range(count):
                product = self.search_products.nth(i) #store all items in product
                title = product.text_content()
                if title and title.strip() == product_name: #match product title removing extra spaces
                    return product
        except Exception as e:
            print(f"Error while checking product existence: {e}")
        return None


    def select_product(self, product_name): #select product and navigate to product selected page
        try:
            count = self.search_products.count()
            for i in range(count):
                product = self.search_products.nth(i)
                title = product.text_content()
                if title and title.strip() == product_name:
                    product.click()
                    return ProductPage(self.page) #ProductPage is imported from my_products_page, class products
            print(f"Product Not Found : {product_name}")
        except Exception as e:
            print(f"Error while selecting Product : {e}")
            return None

    def count_products(self):
        try:
            return self.search_products #all products found
        except Exception as e:
            print(f"Error while getting product : {e}")
            return None



