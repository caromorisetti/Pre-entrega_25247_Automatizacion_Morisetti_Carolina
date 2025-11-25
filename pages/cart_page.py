from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CartPage:

    # Selectores
    _CART_ITEMS = (By.CLASS_NAME, "cart_item")
    _CART_ITEM_NAME = (By.CLASS_NAME,"inventory_item_name")

    def __init__(self,driver):
        self.driver = driver 
        self.wait = WebDriverWait(driver,10)

    def get_products_cart(self):
        products = self.wait.until(EC.visibility_of_all_elements_located(self._CART_ITEMS))
        return products
    
    def get_name_products_cart(self):
        name_products = self.wait.until(EC.visibility_of_element_located(self._CART_ITEM_NAME))
        return name_products.text