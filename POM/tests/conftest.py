from selenium import webdriver
import pytest
from POM.utilities import config_reader

@pytest.fixture()
def setup_and_teardown(request):
    browser=config_reader.get_config("basic info", "browser")
    url=config_reader.get_config("basic info", "url")
    if browser=="chrome":
        driver=webdriver.Chrome()
    else:
        driver=webdriver.Edge()
    driver.maximize_window()
    driver.get(url)
    request.cls.driver=driver
    yield
    driver.quit()
