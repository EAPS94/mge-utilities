# Configuration file for the Sphinx documentation builder.
# For the full list of built-in configuration values, see:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# Agregar la ruta de `src/` para que Sphinx pueda importar los módulos de utilities
sys.path.insert(0, os.path.abspath('../../src'))

# -- Project information -----------------------------------------------------
project = 'mge-utilities'
copyright = '2025, Eduardo P'
author = 'Eduardo P'
release = '1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',  # Documentación automática desde docstrings
    'sphinx.ext.napoleon',  # Soporte para docstrings estilo NumPy/Google
    'sphinx.ext.viewcode'  # Agregar enlaces al código fuente en la documentación
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'  # Cambiamos el tema a "Read the Docs"
html_static_path = ['_static']

# -- Language Configuration --------------------------------------------------
language = 'en' 
