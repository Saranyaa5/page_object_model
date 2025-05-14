import pytest
from OrangeHrm_POM.pages.home_page import HomePage
import time
from OrangeHrm_POM.utilities.excel_reader import get_exceldata
from OrangeHrm_POM.pages.dashboard_page import DashBoardPage
from OrangeHrm_POM.utilities.logger import get_logger

@pytest.mark.usefixtures("setup_teardown")
class TestHome:
    login_data = get_exceldata("C:\page_object_model\OrangeHrm_POM\data\login_data.xlsx","Sheet1")
    logger=get_logger()
    print(login_data)
    def test_valid_user_login(self):
        username,password= self.login_data[0]
        home_page = HomePage(self.driver)
        home_page.enter_user_credentials_in_login(username,password)
        dashboard_page=DashBoardPage(self.driver)

        try:
            assert dashboard_page.check_homepage_logout_visiblity() is True
            self.logger.info("Login is successful")
        except AssertionError:
            self.logger.error("Login is not successful")
            raise

    @pytest.mark.parametrize("username,password", login_data[1:])
    def test_invalid_user_login(self, username, password):
        home_page = HomePage(self.driver)
        home_page.enter_user_credentials_in_login(username, password)
        
        if((username!="Admin" and username!="" )or (password!="admin123" and password!="")):
            try:
                assert home_page.is_invalid_credentials_displayed() is True 
                self.logger.info("Login failed")
            except AssertionError:
                self.logger.error("login success for invalid credentials")
                raise

        elif (username=="" and password==""):
            try:
                both_field_req=home_page.is_username_required_displayed() and home_page.is_password_required_displayed()
                assert both_field_req is True 
                self.logger.info("Login failed")
            except AssertionError:
                self.logger.error("login success for invalid credentials")
                raise
        
        elif username=="":
            try:
                assert home_page.is_username_required_displayed() is True 
                self.logger.info("Login failed")
            except AssertionError:
                self.logger.error("login success for invalid credentials")
                raise
        
        # elif password=="" :
        #     try:
        #         assert home_page.is_password_required_displayed() is True 
        #         self.logger.info("Login failed")
        #     except AssertionError:
        #         self.logger.error("login success for invalid credentials")
        #         raise

 
    
        

