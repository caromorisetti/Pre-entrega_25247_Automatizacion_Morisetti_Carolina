from selenium import webdriver
from utils import do_purchase
import time
from selenium.webdriver.common.by import By

# Test de compra de un producto en la tienda
def test_purchase(logged_in_driver):
    try:
        driver = logged_in_driver
        do_purchase(driver)
        print("Test de compra exitoso")
    except Exception as e:
          print("Error durante la navegacion:", e)
          raise