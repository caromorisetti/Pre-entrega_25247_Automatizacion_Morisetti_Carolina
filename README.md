# Proyecto de Automatización de Pruebas - SauceDemo

## Propósito del Proyecto
El propósito de este proyecto es automatizar las pruebas funcionales del sitio **[SauceDemo](https://www.saucedemo.com/)** utilizando **Selenium** y **Pytest**.  

---

## Tecnologías Utilizadas
- **Python 8.4.1**
- **Selenium 4.36.0**
- **Selenium WebDriver**
- **Pytest**
- **Pytest-HTML** (para generar reportes HTML)

---

## Instrucciones de Instalación de Dependencias

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/caromorisetti/25247_Automatizacion_QA_Morisetti_Carolina.git
2. Acceder al directorio 
3. Crear entorno virtual
  python -m venv venv
- venv\Scripts\activate   # En Windows
- source venv/bin/activate  # En Mac o Linux
4. Instalar dependencias necesarias
   - pip install

## Ejecución de Pruebas con `run_test.py`

Este proyecto incluye un script llamado **`run_test.py`** que permite ejecutar de manera centralizada todas las pruebas y generar un reporte HTML automáticamente.  

## Funcionamiento del script
1. Lista de tests a ejecutar:  
   Dentro del script se define un listado de archivos de prueba:  
   ```python
   test_files = [
       "tests/test_login.py",
       "tests/test_validation.py",
       "tests/test_inventory.py",
       "tests/test_purchase.py"
   ]

2. Argumentos de Pytest:
Se agregan argumentos para:

Ejecutar los tests de manera detallada (-v)

Generar un reporte HTML (--html=report.html)

Crear un reporte autocontenido, incluyendo estilos y recursos (--self-contained-html)
