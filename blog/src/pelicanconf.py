#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'databootcamp team'
SITENAME = u'DataBootCamp'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'pt-br'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

HEADER_COVER = 'static/header.png'

THEME='attila'

STATIC_PATHS=['static']
# Blogroll
LINKS = (('Databootcamp', 'http://databootcamp.com.br/'),
         ('Jupyter Notebook', 'http://jupyter.org/'),)

# Social widget
SOCIAL = (('facebook', 'https://www.facebook.com/databootcampbr/'),
          ('twitter', 'https://twitter.com/databootcampbr'),
          ('linkedin', 'https://www.linkedin.com/company-beta/24780983/'))

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
