import pytest
from selenium import webdriver
from utils import do_login

# Fixture para inicializar y cerrar el navegador
@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
# Fixture para realizar login antes de cada test que lo requiera   
@pytest.fixture
def logged_in_driver(driver):
    do_login(driver)
    return driver