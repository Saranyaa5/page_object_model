from selenium.webdriver.common.by import By
from OrangeHrm_POM.pages.base_page import BasePage

class HomePage(BasePage):
    username_input_field_xpath = (By.XPATH, "//input[contains(@name,'username')]")
    password_input_field_xpath = (By.XPATH, "//input[contains(@name,'password')]")
    login_button_xpath = (By.XPATH, "//button[contains(@class,'orangehrm-login-button')]")
    account_drop_down_xpath=(By.XPATH,"//header//ul/li[contains(@class,'oxd-userdropdown')]")
    logout_button_xpath=(By.XPATH,"//ul[contains(@class, 'oxd-dropdown-menu')]//a[contains(@href, 'logout')]")
    def __init__(self, driver):
        super().__init__(driver)

    def enter_user_credentials_in_login(self, username, password):
        self.wait_for_element_visible(self.username_input_field_xpath, 10)
        self.enter_text(self.username_input_field_xpath, username)
        self.wait_for_element_visible(self.password_input_field_xpath, 10)
        self.enter_text(self.password_input_field_xpath, password)
        self.wait_for_element_clickable(self.login_button_xpath, 10)
        self.click(self.login_button_xpath)

    def check_homepage_logout_visiblity(self):
        self.wait_for_element_clickable(self.account_drop_down_xpath,10)
        self.click(self.account_drop_down_xpath)
        self.wait_for_element_visible(self.logout_button_xpath,10)
        return self.find(self.logout_button_xpath).is_displayed()
