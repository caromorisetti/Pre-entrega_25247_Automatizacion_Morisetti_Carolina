from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
import time
from utils import do_login

# Test de validacion login que utiliza la función reutilizable
def test_login(logged_in_driver):
    driver = logged_in_driver
    try:
        do_login(driver)
    finally:
        driver.quit()