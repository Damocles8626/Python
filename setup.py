# Crear un paquete distribuible
from setuptools import setup

setup(
    name = 'PaqueteOpBásicas',
    version = '1.0',
    description = 'Paquete de operaciones básicas: suma, resta, multiplicación',
    author = 'José',
    packages = ['Paquete_Módulos'] # Carpeta donde está nuestro módulo
    )
# Acceder a la carpeta raíz Python desde el cmd 
# Escribir ahí: python setup.py sdist