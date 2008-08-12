"""
	Copyright (c) 2008, Myles Braithwaite
	All rights reserved.
	
	This software is provided without warranty under the terms of the BSD
	license included in photos/LICENSE.markdown and may be redistributed only under
	the conditions described in the aforementioned license. This license is also
	available online at http://code.google.com/p/django-photo-gallery/wiki/License
	
	Author: Myles Braithwaite
"""

from django.shortcuts import get_object_or_404

from photos.views import render
from photos.models import Gallery, Photo

def photo_detail(request, gallery_slug, photo_slug):
	gallery = get_object_or_404(Gallery, slug__iexact=gallery_slug)
	photo = get_object_or_404(Photo, slug__iexact=photo_slug)
	
	return render(request=request, template_name='photos/photo_detail.html', payload={
		'gallery':	gallery,
		'photo':	photo,
	})
