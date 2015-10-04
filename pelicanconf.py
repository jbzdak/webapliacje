#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os, sys
import pathlib
from tweaked_html_writer.writer import EnchancedRstReader

DIRNAME = os.path.dirname(__file__)

if not DIRNAME in sys.path:
    sys.path.append(DIRNAME)

THEME = str(pathlib.Path(__file__).parent / "themes" / 'jb-pelican-theme')

if not THEME in sys.path:
    sys.path.append(THEME)

print(sys.path)

import blog_utils

PLUGIN_PATHS = [str(pathlib.Path(DIRNAME) / 'pelican-plugins')]


AUTHOR = 'Jacek Bzdak'
SITENAME = 'Projektowanie Webaplikacji'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Warsaw'

DEFAULT_LANG = 'pl'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

READERS = {
  'rst': EnchancedRstReader,
  'html': None
}

JINJA_EXTENSIONS = [
    'jinja2.ext.with_'
]


JINJA_FILTERS = {
    "tagsort_by_popularity": blog_utils.tagsort_by_popularity,
    "as_dict": blog_utils.as_dict,
    "truncate_words": blog_utils.truncate
}

ARTICLE_EXCLUDES = ['downloads']

STATIC_PATHS = ['downloads']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
