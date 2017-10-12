#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Daniel Rivero'
AUTHOR_EMAIL = u'rivero1dan@gmail.com'
SITENAME = 'dirac is an anagram to..'
#SITEURL = 'dirac.one'
THEME_STATIC_DIR = 'theme'
THEME = 'theme/voce'
PATH = 'content'

TIMEZONE = 'America/Caracas'
DEFAULT_LANG = 'en'

# Formating URLs
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

# Theme related options
USER_LOGO_URL = '/dirac_page.gif'
GLOBAL_KEYWORDS = ['Linux','Networking','Security','Telecommunication']
FUZZY_DATES = 'true'
TAGS_URL = 'tags.html'
ARCHIVES_URL = 'archives.html'
MANGLE_EMAILS = True
GOOGLE_ANALYTICS_PROP = 'dirac.one'
GOOGLE_ANALYTICS_ID = 'UA-108034005-1'

# Personalised Theme
CSS_FILE = '/theme/style.css'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Plugins
PLUGIN_PATHS =['theme/voce/plugins']
PLUGINS = ['assets']

# Blogroll
LINKS = (('Home', '/index.html'),
         ('About Me', '/pages/about.html'),
         ('CV', '/files/DanielRivero_CV.pdf'),
         ('Something cool', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/River0Dan'),
          ('telegram', u'https;//t.me/dirac1'),
          ('Email', 'mailto:rivero1dan@gmail.com'),)

STATIC_PATHS = ['/files/favicon.ico', '/files/DanielRivero_CV.pdf','/files/dirac_page.gif']

EXTRA_PATH_METADATA = {
    '/files/favicon.ico': {'path': 'favicon.ico'},
    '/files/DanielRivero_CV.pdf': {'path': 'DanielRivero_CV.pdf'},
    '/files/dirac_page.gif': {'path': 'dirac-page.gif'},
}

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
