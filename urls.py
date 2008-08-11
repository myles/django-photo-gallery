"""
	Copyright (c) 2008, Myles Braithwaite
	All rights reserved.
	
	This software is provided without warranty under the terms of the BSD
	license included in photos/LICENSE.markdown and may be redistributed only under
	the conditions described in the aforementioned license. This license is also
	available online at http://code.google.com/p/django-photo-gallery/wiki/License
	
	Author: Myles Braithwaite
"""

from django.conf.urls.defaults import *

urlpatterns = patterns('',
	url(r'^comments/$',
		view	= 'photos.views.comments.list',
		name	= 'photo_gallery_comment',
	),
	url(r'^galleries/$',
		view	= 'photos.views.gallery.archive',
		name	= 'photo_gallery_archive',
	),
	url(r'^(?P<gallery_slug>[-\w]+)/gallery/(?P<photo_slug>[-\w]+)/$',
		view	= 'photos.views.photo.detail',
		name	= 'photo_gallery_photo_detail',
	),
	url(r'^(?P<gallery_slug>[-\w]+)/gallery/$',
		view	= 'photos.views.gallery.detail',
		name	= 'photo_gallery_detail',
	),
	url(r'^(?P<gallery_slug>[-\w]+)/$',
		view	= 'photos.views.gallery.title',
		name	= 'photo_gallery_title',
	),
	url(r'^$', 
		view	= 'photos.views.gallery.index',
		name	= 'photo_gallery_index',
	),
)