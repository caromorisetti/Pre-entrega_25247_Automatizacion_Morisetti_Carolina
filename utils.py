from selenium.webdriver.common.by import By 
import time

# Función reutilizable de login
def do_login(driver):
    try:
        # Login
        driver.get("https://www.saucedemo.com/")
        # Espera time para que cargue la pagina
        time.sleep(2)
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        time.sleep(2)
        driver.find_element(By.ID, "login-button").click()
        # Validacion de la redireccion de la pagina
        assert '/inventory.html' in driver.current_url
        time.sleep(2)    
        print("Login exitoso y validado correctamente")
    except Exception as e:
        print("Error durante el login:", e)
        raise