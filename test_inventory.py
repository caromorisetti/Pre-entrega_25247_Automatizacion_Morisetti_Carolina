from selenium import webdriver
from test_login import do_login
from selenium.webdriver.common.by import By

def test_inventory(logged_in_driver):
     try: 
          driver = logged_in_driver
          # Espera implicita
          driver.implicitly_wait(5)
          do_login(driver)
          # Navegamos a la sección de productos y validamos que se cargaron
          productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
          assert len(productos) > 0    
          print("Test exitoso")
     except Exception as e:
          print("Error durante la navegacion:", e)
          raise
     finally:
          driver.quit()