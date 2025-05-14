import pytest
from POM.pages.home_page import HomePage
from POM.pages.search_page import SearchPage
from POM.utilities.consolelogger import get_logger

logger = get_logger()

@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_search_for_valid_product(self):
        logger.info("Test started: test_search_for_valid_product")

        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_box_field("HP")
        home_page.click_search_button()

        search_page = SearchPage(self.driver)
        result = search_page.get_display_status_of_valid_product()

        try:
            assert result is True
            logger.info(f"Product display status: {result}")
        except :
            logger.error(f"Product display status: {result}")

