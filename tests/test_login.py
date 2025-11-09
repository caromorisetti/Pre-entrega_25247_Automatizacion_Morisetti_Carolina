from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from pages.login_page import LoginPage
from utils.data import csv_login

@pytest.mark.parametrize("user,password,should_work",csv_login("data/data_login.csv"))
def test_login(logged_in_driver,user,password,should_work):
    driver = logged_in_driver
    
    if should_work == 'true':
        assert "inventory" in driver.current_url, "No se redirigio al inventario"
    elif should_work == 'false':
        message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
        assert "Epic sadface: Username and password do not match any user in this service" in message, "El mensaje de error no es correcto"
    