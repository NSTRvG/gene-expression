from setuptools import setup, find_packages

setup(
    name="expresion_genica",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "matplotlib",
        "seaborn",
        "numpy",
        "openpyxl"
    ],
    description="Paquete para análisis de expresión génica y visualización de datos.",
    author="Nestor Velandia & Felipe Vásquez",

)
