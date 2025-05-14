from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find(self, by_locator):
        return self.driver.find_element(*by_locator)

    def finds(self, by_locator):
        return self.driver.find_elements(*by_locator)

    def click(self, by_locator):
        self.find(by_locator).click()

    def enter_text(self, by_locator, text):
        element = self.find(by_locator)
        element.clear()
        element.send_keys(text)

    def get_element_text(self, by_locator):
        return self.find(by_locator).text

    def is_element_visible(self, by_locator):
        return self.find(by_locator).is_displayed()
    
    def wait_for_element_visible(self, by_locator, timeout):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locator))

    def wait_for_element_clickable(self, by_locator, timeout):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(by_locator))
