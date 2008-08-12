"""
	Copyright (c) 2008, Myles Braithwaite
	All rights reserved.
	
	This software is provided without warranty under the terms of the BSD
	license included in photos/LICENSE.markdown and may be redistributed only under
	the conditions described in the aforementioned license. This license is also
	available online at http://code.google.com/p/django-photo-gallery/wiki/License
	
	Author: Myles Braithwaite
"""

from django.core.paginator import QuerySetPaginator, InvalidPage
from django.contrib.comments.models import FreeComment

from photos.views import render
from photos.models import Photo

def list(request, page=0):
	comments = FreeComment.objects.filter(content_type=Photo, approved=True, is_public=True)
	
	paginator = QuerySetPaginator(comments, 25, allow_empty_first_page=True)
	if not page:
		page = request.GET.get('page', 1)
		try:
			page_number = int(page)
		except ValueError:
			if page == 'last':
				page_number = paginator.num_pages
			else:
				raise Http404
		
		try:
			page_obj = paginator.page(page_number)
		except InvalidPage:
			raise Http404
	
	return render(request=request, template_name='photos/comment_list.html', payload={
		'comments':	comments,
		'is_paginated':		page_obj.has_other_pages(),
		'results_per_page':	paginator.per_page,
		'has_next':			page_obj.has_next(),
		'has_previous':		page_obj.has_previous(),
		'page':				page_obj.number,
		'next':				page_obj.next_page_number(),
		'previous':			page_obj.previous_page_number(),
		'first_on_page':	page_obj.start_index(),
		'last_on_page':		page_obj.end_index(),
		'pages':			paginator.num_pages,
		'hits':				paginator.count,
		'page_range':		paginator.page_range,
	})
