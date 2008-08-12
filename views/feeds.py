"""
	Copyright (c) 2008, Myles Braithwaite
	All rights reserved.
	
	This software is provided without warranty under the terms of the BSD
	license included in photos/LICENSE.markdown and may be redistributed only under
	the conditions described in the aforementioned license. This license is also
	available online at http://code.google.com/p/django-photo-gallery/wiki/License
	
	Author: Myles Braithwaite
"""

import datetime

from django.utils.translation import ugettext_lazy as _
from django.utils import feedgenerator
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse

from photos.models import Photo, Gallery, Module

def photos_feed(request, feedclass):
	current_site_name = Site.objects.get_current().name
	current_site_domain = Site.objects.get_current().domain
	description = Module.objects.get(module_type=2)
	TODAY = datetime.date.today()
	
	photos = Photo.objects.all()[:15]
	
	feed = feedcass(
		title = "%s - %s" % (current_site_name, _('Photos')),
		link = reverse('photo_gallery_index'),
		description = description,
		copyright = 'Copyright %s' % TODAY.year,
		feed_url = "%s/%s" % (current_site_domain, reverse('photo_gallery_feed_photos'))
	)
	
	for photo in photos:
		feed.add_item(
			title = u"%s" % photo.title,
			link = photo.get_absolute_url(),
			description = u"%s" % photo.description,
			pubdate = photo.created,
			unique_id = photo.get_absolute_url(),
			categories = gallery.title,
		)
