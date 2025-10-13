from selenium import webdriver
import time

driver = webdriver.Chrome()

try:
    # Validacion del titulo de la pagina
    driver.get("https://www.saucedemo.com/")
    print("El titulo es: ", driver.title)
    assert driver.title == "Swag Labs"
    time.sleep(4)
finally:
    driver.quit()