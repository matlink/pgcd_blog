#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Matlink'
SITENAME = u'Le Parti des Geeks Cartésiens Démocrates'
SITEURL = ''
SITESUBTITLE = u"Blog d'un ensemble universitaire et passioné"

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'

THEME = "customtheme"

STATIC_PATHS = ['doc','images']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PIWIK_URL = "fr.matlink.fr/piwik"
PIWIK_SSL_URL = "fr.matlink.fr/piwik"
PIWIK_SITE_ID = 1

PLUGIN_PATHS = ['./plugins/']

#Comments plugin
ISSO_SERVER="fr.matlink.fr/comments"


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
