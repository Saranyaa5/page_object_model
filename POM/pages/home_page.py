from seleniumpagefactory.Pagefactory import PageFactory
from POM.utilities.consolelogger import get_logger

class HomePage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger()
        super().__init__()  

    locators = {
        'search_box_field': ('NAME', 'search'),
        'search_button': ('XPATH', "//button[@class='btn btn-default btn-lg']")
    }

    def enter_product_into_search_box_field(self, product_name):
        self.logger.info(f"Entering product name: {product_name}")
        self.search_box_field.click()
        self.search_box_field.clear()
        self.search_box_field.send_keys(product_name)

    def click_search_button(self):
        self.logger.info("Clicking the search button")
        self.search_button.click()
