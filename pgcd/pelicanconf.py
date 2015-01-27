#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Matlink'
SITENAME = u'Le Parti des Geeks Cartésiens Démocrates'
SITEURL = ''
SITESUBTITLE = u"Blog d'un parti universitaire et passioné"

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'

THEME = "customtheme"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll

LINKS = (('Pelican', 'http://getpelican.com/', '/theme/images/icons/pelican_logo.png'),)

# Social widget
SOCIAL = (
		('Twitter', 'https://twitter.com/M4tlink'),
		('Facebook', 'https://www.facebook.com/partigeekscartesiensdemocrates'),
		)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
