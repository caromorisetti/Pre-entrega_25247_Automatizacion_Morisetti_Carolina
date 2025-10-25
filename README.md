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
   pip install
5. pip install selenium
6. pip install webdriver-manager
7.pip install pytest pytest-html

## Comando para ejecutar las pruebas
Pruebas
 - py -m pytest (nombre del test)

Reporte de pruebas
 - pytest -v --html=reporte.html
