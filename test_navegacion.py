from selenium import webdriver
from test_login import do_login
from selenium.webdriver.common.by import By

def test_navegacion():
     driver = webdriver.Chrome()
     # Espera implicita
     driver.implicitly_wait(5)
     do_login(driver)
     try:
          # Interacciones
          productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
          productos[0].find_element(By.TAG_NAME, "button").click()
          carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
          assert carrito == '1'    
          print("Test exitoso")
     except Exception as e:
          print("Error durante la navegacion:", e)
          raise
     finally:
          driver.quit()