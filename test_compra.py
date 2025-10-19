from selenium import webdriver
from test_login import do_login
import time
from selenium.webdriver.common.by import By

def test_compra():
    driver = webdriver.Chrome()
    try:
          do_login(driver)
          # Agregamos un producto al carrito
          driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
          driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
          carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
          time.sleep(2)
          # Validamos que el producto esté en el carrito
          assert carrito == "1"
          producto = driver.find_element(By.CLASS_NAME, "cart_item").text
          # Verificar que el producto correcto está en el carrito
          producto = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
          assert producto == "Sauce Labs Bolt T-Shirt"
          print("Test de compra exitoso")
                  
    except Exception as e:
          print("Error durante la navegacion:", e)
          raise
