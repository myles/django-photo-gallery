"""
	Copyright (c) 2008, Myles Braithwaite
	All rights reserved.
	
	This software is provided without warranty under the terms of the BSD
	license included in photos/LICENSE.markdown and may be redistributed only under
	the conditions described in the aforementioned license. This license is also
	available online at http://code.google.com/p/django-photo-gallery/wiki/License
	
	Author: Myles Braithwaite
"""

from django import template

register = template.Library()

@register.simple_tag
def photo_media_prefix():
	"""
	Returns the string contained in the setitng PHOTOS_GALLERY_MEDIA_PREFIX.
	
	This code is a copy of the Django Admin template tag `admin_media_prefix`.
	"""
	try:
		from django.conf import settings
	except ImportError:
		return ''
	return settings.PHOTOS_GALLERY_MEDIA_PREFIX
