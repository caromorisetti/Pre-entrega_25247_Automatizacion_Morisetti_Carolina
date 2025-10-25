from selenium import webdriver
from utils import get_products
from selenium.webdriver.common.by import By

# Test de navegacion y verificacion de productos en la pagina de inventario
def test_inventory(logged_in_driver):
     try: 
          driver = logged_in_driver
          driver.implicitly_wait(3)
          products = get_products(driver)
          assert len(products) > 0    
          print("Test de inventario exitoso: Productos cargados correctamente.")
     except Exception as e:
          print("Error durante la navegacion:", e)
          raise