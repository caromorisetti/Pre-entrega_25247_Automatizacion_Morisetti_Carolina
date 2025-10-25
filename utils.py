from selenium.webdriver.common.by import By 
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Función de login
def do_login(driver):
        wait = WebDriverWait(driver, 10)
        # Login
        driver.get("https://www.saucedemo.com/")
        # Espera explícita para los elementos de login
        wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()
        wait.until(EC.url_contains("/inventory.html"))
        # Validacion de la redireccion de la pagina
        assert '/inventory.html' in driver.current_url
    
# Funcion de compra completo   
def do_purchase(driver):
          # Agregamos un producto al carrito
          driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
          driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
          carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
          # Validamos que el producto esté en el carrito
          assert carrito == "1"
          producto = driver.find_element(By.CLASS_NAME, "cart_item").text
          # Verificar que el producto correcto está en el carrito
          producto = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
          assert producto == "Sauce Labs Bolt T-Shirt"
          # Espera antes de proceder al checkout
          time.sleep(2)
          # Procedemos al checkout
          driver.find_element(By.ID, "checkout").click()
          driver.find_element(By.ID, "first-name").send_keys("Carola")
          driver.find_element(By.ID, "last-name").send_keys("Perez")
          driver.find_element(By.ID, "postal-code").send_keys("12345")
          driver.find_element(By.ID, "continue").click()
          driver.find_element(By.ID, "finish").click()
          # Validamos que la compra se completó
          mensaje = driver.find_element(By.CLASS_NAME, "complete-header").text
          assert mensaje == "Thank you for your order!"
          time.sleep(2)
                    
# Función para obtener la lista de productos en inventario    
def get_products(driver):
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    return products

# Función para validar la presencia del menú
def validate_menu(driver):
    menu = driver.find_element(By.ID, "react-burger-menu-btn").is_displayed()
    return menu

# Función para validar la presencia del filtro
def validate_filter(driver):
    filter = driver.find_element(By.CLASS_NAME, "product_sort_container").is_displayed()
    return filter