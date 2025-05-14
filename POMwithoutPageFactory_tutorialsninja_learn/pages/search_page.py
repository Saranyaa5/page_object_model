from selenium.webdriver.common.by import By
class SearchPage:
    def __init__(self,driver):
        self.driver=driver
    display_Status_of_valid_product_link_text="HP LP3065"

    def get_display_status_of_valid_product(self):
        try:
            return self.driver.find_element(By.LINK_TEXT, self.display_Status_of_valid_product_link_text).is_displayed()
        except:
            return False
