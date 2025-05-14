import pytest
from selenium import webdriver
from OrangeHrm_POM.utilities.config_reader import get_config_data

@pytest.fixture()
def setup_teardown(request):
  browser=get_config_data("basic info","browser")
  url=get_config_data("basic info","url")
  
  if browser=="chrome":
    driver=webdriver.Chrome()
  elif browser=="firefox":
    driver=webdriver.Firefox()
  else:
    driver=webdriver.Edge()
  
  driver.maximize_window()
  driver.get(url)

  request.cls.driver= driver
  yield
  driver.quit()

  
