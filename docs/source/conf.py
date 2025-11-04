# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'M.Biodiv.441 Evolutionary Ecology'
author = 'Bastian Heimburger'
release = '0.1'
version = '0.1.1'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.youtube',
    'sphinx_tabs.tabs',
    'sphinx_copybutton',
    'sphinxcontrib.images',
    "sphinx.ext.napoleon",
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

#html_theme = 'sphinx_rtd_theme'
html_theme = "sphinxawesome_theme"

#html_css_files = [
#    'custom.css',
#]
