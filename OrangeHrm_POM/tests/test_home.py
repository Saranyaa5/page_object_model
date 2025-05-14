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
    
        

