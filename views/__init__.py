"""
	Copyright (c) 2008, Myles Braithwaite
	All rights reserved.
	
	This software is provided without warranty under the terms of the BSD
	license included in photos/LICENSE.markdown and may be redistributed only under
	the conditions described in the aforementioned license. This license is also
	available online at http://code.google.com/p/django-photo-gallery/wiki/License
	
	Author: Myles Braithwaite
"""

from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from photos.models import Module

def render(request, template_name, payload):
	footer = Module.objects.get(module_type=1)
	description = Module.objects.get(module_type=2)
	payload.update({
		'footer'		: footer,
		'description'	: description,
	})
	return render_to_response(template_name, payload, context_instance=RequestContext(request))
