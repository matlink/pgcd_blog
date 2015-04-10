#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Matlink'
SITENAME = u'Le PGCD'
COOLSITENAME = u'Le <span class="acronyme">P</span>arti des <span class="acronyme">G</span>eeks <span class="acronyme">C</span>artésiens <span class="acronyme">D</span>émocrates'
SITEURL = ''
SITESUBTITLE = u"Blog universitaire d'un groupe de potes passionnés"

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'

THEME = "new_customtheme"

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

#Comments plugin
ISSO_SERVER="fr.matlink.fr/comments"


# Blogroll

LINKS = (	('Pelican', 'http://getpelican.com/', '/theme/images/icons/pelican_logo.png'),
			('OpenMailBox', 'https://openmailbox.org', '/theme/images/icons/openmailbox_logo.png'),
			('NullPointerException','https://blog.imirhil.fr','/theme/images/icons/aeris.png'),
			('Le Blog de Genma','http://genma.free.fr','/theme/images/icons/genma.png')
		)

# Social widget
SOCIAL = (
		('Twitter', 'https://twitter.com/M4tlink'),
		('Facebook', 'https://www.facebook.com/partigeekscartesiensdemocrates'),
		)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
