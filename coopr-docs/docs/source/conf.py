# -*- coding: utf-8 -*-
#
# Coopr documentation build configuration file, created by
# sphinx-quickstart on Thu Dec  5 11:56:37 2013. Modified manually 02/01/2014
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
import subprocess
from datetime import datetime

def get_sdk_version():
    # Sets the Build Version
    grep_version_cmd = "grep '<version>' ../../../pom.xml | awk 'NR==1;START{print $1}'"
    version = None
    full_version = None
    try:
        full_version = subprocess.check_output(grep_version_cmd, shell=True).strip().replace("<version>", "").replace("</version>", "")
        version = full_version.replace("-SNAPSHOT", "")
    except:
        pass
    return version, full_version

def print_sdk_version():
    version, full_version = get_sdk_version()
    if version == full_version:
        print "SDK Version: %s" % version
    elif version and full_version: 
        print "SDK Version: %s (%s)" % (version, full_version)
    else:
        print "Could not get version (%s), full version (%s) from grep" % (version, full_version)

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinxcontrib.fulltoc',
    'sphinxcontrib.googleanalytics',
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.pngmath',
    'sphinx.ext.ifconfig',
]

# Google analytics configuration
googleanalytics_id = 'UA-27787617-1'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Coopr'
copyright = u'2014-%s Cask Data, Inc.' % datetime.now().year

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
# version = '0.9.9'
# The full version, including alpha/beta/rc tags.
# release = '0.9.9 Beta'

version, release = get_sdk_version()

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'en_CDAP'
locale_dirs = ['_locale/']

# A string of reStructuredText that will be included at the end of every source file that
# is read. This is the right place to add substitutions that should be available in every
# file. 
rst_epilog = """
.. |bold-version| replace:: **%(version)s**

.. |italic-version| replace:: *%(version)s*

.. |literal-version| replace:: ``%(version)s``

.. |literal-release| replace:: ``%(release)s``

.. role:: gp
.. |$| replace:: :gp:`$`

.. |http:| replace:: http:

.. |(TM)| unicode:: U+2122 .. trademark sign
   :ltrim:

.. |(R)| unicode:: U+00AE .. registered trademark sign
   :ltrim:

.. |copyright| replace:: %(copyright)s

""" % {'version': version, 
       'release': release,
       'copyright': copyright,
       }

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# The default language to highlight source code in.
highlight_language = 'java'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# html_theme = 'nature'
html_theme = 'cdap'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# versions points to the JSON file on the webservers
# versions_data is used to generate the JSONP file at http://docs.cask.co/cdap/json-versions.js
# format is a dictionary, with "development" and "older" lists of lists, and "current" a list, 
# the inner-lists being the directory and a label

html_theme_options = {
  "versions":"http://docs.cask.co/%s/json-versions.js" % project.lower(),
  "versions_data":
    { "development": 
        [ ["0.9.10-SNAPSHOT", "0.9.10"], ], 
      "current": ["0.9.9", "0.9.9"], 
      "older": 
        [ ["0.9.8", "0.9.8"], ],
    },
}

def get_json_versions():
    return "versionscallback(%s);" % html_theme_options["versions_data"]

def print_json_versions():
    print "versionscallback(%s);" % html_theme_options["versions_data"]

def print_json_versions_file():
    head, tail = os.path.split(html_theme_options["versions"])
    print tail

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []
html_theme_path = ['_themes']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None
html_short_title = u"%s Documentation v%s" % (project, version)

# A shorter title for the sidebar section, preceding the words "Table of Contents".
# html_short_title_toc = u"%s Documentation" % project
html_short_title_toc = ''

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None
html_favicon = '_static/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}
html_sidebars = {'**': ['globaltoc.html', 'relations.html', 'downloads.html', 'searchbox.html'],}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
html_domain_indices = True

# If false, no index is generated.
html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False
html_copy_source = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'Cooprdoc'

# This context needs to be created in each child conf.py. At a minimum, it needs to be 
# html_context = {"html_short_title_toc":html_short_title_toc}
# This is because it needs to be set as the last item.
html_context = {"html_short_title_toc":html_short_title_toc}

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('misc/jboss-automator-script', 'JBoss-Automator-Script.tex', u'JBoss Automator Script Documentation',
   u'Cask Data, Inc.', 'howto'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = '_static/logo.png'

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'coopr', u'Documentation',
     [u'Cask Data, Inc.'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'Coopr', u'Documentation',
   u'Cask Data, Inc.', 'Coopr', 'Moder cluster provisioning and lifecycle management system.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'http://docs.python.org/': None}
