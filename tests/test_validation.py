from selenium.webdriver.common.by import By 
from selenium import webdriver
import time
from utils import validate_menu, validate_filter

# Test de validacion de titulo de la pagina principal, menu y filtro en la pagina de inventario
def test_validation(logged_in_driver):
    try:
        driver = logged_in_driver
        time.sleep(2)
        assert driver.title == "Swag Labs"
        print("Titulo de pagina de inventario correcto")
        menu = validate_menu(driver)
        assert menu == True
        print("Validacion de menu exitosa")   
        filter = validate_filter(driver)
        assert filter == True
        print("Validacion de filtro exitosa")
    except Exception as e:
        print("Error durante la navegacion:", e)
        raise