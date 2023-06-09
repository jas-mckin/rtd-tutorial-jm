# Configuration file for the Sphinx documentation builder.


release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

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

# - add logo to top of site
# html_theme = 'sphinx_rtd_theme'
# html_static_path = ['_static']
# html_logo = 'images/ENA_Logo_tagline.png'
# -html_theme_options = {
#    'logo_only': True,
#    'display_version': False,
#}

# -- Project information
project = 'ena-pathogen-docs'
copyright = '2023, European Nucleotide Archive (ENA), Licensed under the Apache License 2.0'
author = 'European Nucleotide Archive (ENA)'

# makes tabs possible
extensions = ['sphinx_tabs.tabs']
sphinx_tabs_valid_builders = ['linkcheck']