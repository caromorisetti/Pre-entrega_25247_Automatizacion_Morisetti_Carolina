from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class InventoryPage:
    # URL
    URL = "https://www.saucedemo.com/inventory.html"
    # Selectores
    _INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")
    _BUTTON_ADD_TO_CART = (By.CLASS_NAME, "btn_inventory")
    _BUTTON_REMOVE_FROM_CART = (By.CLASS_NAME, "btn_inventory")
    _SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    _INVENTORY_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    _SHOPPING_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")    
    # Constructor
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)   
    # Método para obtener los productos en inventario
    def get_products(self):
        # Esperar a que los productos estén visibles
        self.wait.until(EC.visibility_of_all_elements_located(self._INVENTORY_ITEM))
        products = self.driver.find_elements(*self._INVENTORY_ITEM)
        return products
    