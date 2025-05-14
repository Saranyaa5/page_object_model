from selenium.webdriver.common.by import By
class HomePage:
    def __init__(self,driver):
        self.driver=driver

    search_box_fieid_name="search"
    search_button_xpath="//button[@class='btn btn-default btn-lg']"

    def enter_product_into_search_box_feild(self,product_name):
        self.driver.find_element(By.NAME,self.search_box_fieid_name).click()
        self.driver.find_element(By.NAME,self.search_box_fieid_name).clear()
        self.driver.find_element(By.NAME,self.search_box_fieid_name).send_keys(product_name)

    def click_search_button(self):
        self.driver.find_element(By.XPATH,self.search_button_xpath).click()
