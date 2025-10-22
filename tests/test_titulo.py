from selenium import webdriver
import time

# Test de validacion del titulo de la pagina
def test_titulo(logged_in_driver):
    try:
        driver = logged_in_driver
        driver.get("https://www.saucedemo.com/")
        print("El titulo es: ", driver.title)
        assert driver.title == "Swag Labs"
        time.sleep(2)
    except Exception as e:
        print("Error durante en el titulo:", e)   
    finally:
        driver.quit()