from selenium.webdriver.common.by import By 
from selenium import webdriver
from utils import do_login
import time

# Test de validacion de menu y filtro en la pagina de inventario
def test_validacion(logged_in_driver):
    try:
        driver = logged_in_driver
        # Login
        do_login(driver)
        time.sleep(1)
        # Validacion de menu
        menu = driver.find_element(By.ID, "react-burger-menu-btn").is_displayed()
        assert menu == True    
        # Validacion de filtro
        filtro = driver.find_element(By.CLASS_NAME, "product_sort_container").is_displayed()
        assert filtro == True
        print("Validacion de menu y filtro exitosa")
    except Exception as e:
        print("Error durante validacion de menu y filtro:", e)
        raise
    finally:
        driver.quit()