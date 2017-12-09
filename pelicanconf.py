#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Daniel Rivero'
AUTHOR_EMAIL = u'rivero1dan@gmail.com'
SITENAME = 'dirac is an anagram to..'
#SITEURL = 'dirac.one'
THEME_STATIC_DIR = 'theme'
THEME = 'theme/voce'

TIMEZONE = 'America/Caracas'
DEFAULT_LANG = 'en'

# Formating URLs
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

# Theme related options
USER_LOGO_URL = '/files/banner.png'
GLOBAL_KEYWORDS = ['Linux','Networking','Security','Telecommunication']
FUZZY_DATES = 'true'
TAGS_URL = 'tags.html'
ARCHIVES_URL = 'archives.html'
MANGLE_EMAILS = True
GOOGLE_ANALYTICS_PROP = 'dirac.one'
GOOGLE_ANALYTICS_ID = 'UA-108034005-1'

# SITEMAP
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
          }
# Personalised Theme
#CSS_FILE = '/style.css'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'

# Plugins
PLUGIN_PATHS =['theme/voce/plugins','plugin/pelican-plugins']
PLUGINS = ['assets','sitemap']

# Blogroll
LINKS = (('Home', '/index.html'),
         ('About Me', '/pages/about.html'),
         ('Résumé', '/pages/cv.html'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/River0Dan'),
          ('Email', 'mailto:rivero1dan@gmail.com'),)

STATIC_PATHS = ['files/favicon-16x16.png','files/favicon-32x32.png','files/favicon.ico', 'files/CV_DR_ES.pdf','files/CV_DR_EN.pdf','files/banner.png']

EXTRA_PATH_METADATA = {
    'files/favicon.ico': {'path': 'favicon.ico'},
    'files/favicon-16x16.png': {'path': 'favicon-16x16.png'},
    'files/favicon-32x32.png': {'path': 'favicon-32x32.png'},
    'files/favicon-96x96.png': {'path': 'favicon-96x96.png'},
#    'files/CV_DR_EN.pdf': {'path': 'CV_DR_EN.pdf'},
#    'files/CV_DR_ES.pdf': {'path': 'CV_DR_ES.pdf'},
#    'files/banner.png'  : {'path': 'files/banner.png'},
}

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
