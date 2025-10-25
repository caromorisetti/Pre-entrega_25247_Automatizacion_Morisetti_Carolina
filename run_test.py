import pytest

#Lista archivos a ejecutar
test_files = [
    "tests/test_login.py",
    "tests/test_validation.py",
    "tests/test_inventory.py",
    "tests/test_purchase.py"
]
#Argumento para ejecutar las pruebas: Reporte HTML y archivo
pytest_args = test_files + ["-v", "--html=report.html", "--self-contained-html"]    
pytest.main(pytest_args)