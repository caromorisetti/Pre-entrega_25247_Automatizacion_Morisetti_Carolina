from selenium import webdriver
from tests.test_login import do_login
import time
from selenium.webdriver.common.by import By

def test_compra(logged_in_driver):
    try:
          driver = logged_in_driver
          # Login
          do_login(driver)
          # Agregamos un producto al carrito
          driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
          driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
          carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
          # Validamos que el producto esté en el carrito
          assert carrito == "1"
          producto = driver.find_element(By.CLASS_NAME, "cart_item").text
          # Verificar que el producto correcto está en el carrito
          producto = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
          assert producto == "Sauce Labs Bolt T-Shirt"
          time.sleep(2)
          # Procedemos al checkout
          driver.find_element(By.ID, "checkout").click()
          driver.find_element(By.ID, "first-name").send_keys("Carola")
          driver.find_element(By.ID, "last-name").send_keys("Perez")
          driver.find_element(By.ID, "postal-code").send_keys("12345")
          driver.find_element(By.ID, "continue").click()
          driver.find_element(By.ID, "finish").click()
          # Validamos que la compra se completó
          mensaje = driver.find_element(By.CLASS_NAME, "complete-header").text
          assert mensaje == "Thank you for your order!"
          time.sleep(2)
          print("Test de compra exitoso")               
    except Exception as e:
          print("Error durante la navegacion:", e)
          raise
