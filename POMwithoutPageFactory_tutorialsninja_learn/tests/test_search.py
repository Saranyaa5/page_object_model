import pytest
from selenium.webdriver.common.by import By

from pages.home_apge import HomePage
from pages.search_page import SearchPage

@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_search_for_valid_product(self):
        home_page=HomePage(self.driver)
        home_page.enter_product_into_search_box_feild("HP")
        home_page.click_search_button()
        search_page=SearchPage(self.driver)
        search_page.get_display_status_of_valid_product()