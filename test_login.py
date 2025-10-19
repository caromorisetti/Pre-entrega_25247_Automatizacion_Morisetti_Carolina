from selenium import webdriver
import time
from selenium.webdriver.common.by import By

def test_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    try:
        # Login
        driver.get("https://www.saucedemo.com/")
        time.sleep(3)
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(3)
        # Validacion de la redireccion de la pagina
        assert '/inventory.html' in driver.current_url    
        print("Login exitoso y validado correctamente")
    except Exception as e:
        print("Error durante el login:", e)
        raise
    finally:
        driver.quit()