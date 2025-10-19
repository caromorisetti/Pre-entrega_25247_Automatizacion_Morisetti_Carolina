from selenium import webdriver
import time


def test_titulo():
    driver = webdriver.Chrome()

    try:
        # Validacion del titulo de la pagina
        driver.get("https://www.saucedemo.com/")
        print("El titulo es: ", driver.title)
        assert driver.title == "Swag Labs"
        time.sleep(2)
    finally:
        driver.quit()