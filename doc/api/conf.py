import os
import sys
sys.path.insert(0, os.path.abspath('../../src'))
# For soupparser in lxml.html.ElementSoup module:
sys.path.insert(1, os.path.abspath('../../src/lxml/html'))

from lxml import __version__ as lxml_version

# -- Project information -----------------------------------------------------

project = 'lxml'
copyright = '2020, lxml dev team'
author = 'lxml dev team'
version = lxml_version


# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx_rtd_theme',
]

language = 'en'

exclude_patterns = ['_build']


# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'

html_logo = '../html/python-xml.png'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']


# -- Extension configuration -------------------------------------------------

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
#todo_include_todos = True
