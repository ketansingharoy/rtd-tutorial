# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'SeisScan'
copyright = '2024, Ketan'
author = 'Ketan'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',          # To generate autodocs
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',         # For auto-doc configuration
    'sphinx.ext.viewcode',
    'sphinx.ext.mathjax',          # autodoc with maths
    'sphinx_copybutton',
]
napoleon_google_docstring = False   # Turn off googledoc strings
napoleon_numpy_docstring = True     # Turn on numpydoc strings
napoleon_use_ivar = True 	     # For maths symbology
autosummary_generate = True

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
