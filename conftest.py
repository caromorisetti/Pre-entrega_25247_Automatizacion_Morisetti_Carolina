import pytest
from selenium import webdriver
from utils import do_login

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
    
@pytest.fixture
def logged_in_driver(driver):
    return driver