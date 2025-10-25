from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest

# Test de validacion login que utiliza la función reutilizable
def test_login(logged_in_driver):
    try:
        driver = logged_in_driver
        print("Test de Login exitoso y redireccion correcta a la pagina de inventario")
    except Exception as e:
        print("Error durante el login:", e)
        raise