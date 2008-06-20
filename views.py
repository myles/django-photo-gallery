from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from photos.models import Gallery, Photo, Module

def gallery_index(request):
	galleries = Gallery.objects.all()[:6]
	favorites = Photo.objects.filter(favorite=True)[:6]
	
	return render(request, 'photos/gallery_index.html', { 'galleries': galleries, 'favorites': favorites })

def gallery_title(request, gallery_slug):
	gallery = get_object_or_404(Gallery, slug__iexact=gallery_slug)
	
	return render(request, 'photos/gallery_title.html', { 'gallery': gallery })

def gallery_detail(request, gallery_slug):
	gallery = get_object_or_404(Gallery, slug__iexact=gallery_slug)
	photos = Photo.objects.filter(gallery=gallery)[:25]
	
	return render(request, 'photos/gallery_detail.html', { 'gallery': gallery, 'photos': photos })

def render(request, tempalte_name, payload):
	footer = Module.objects.get(module_type=1)
	description = Module.objects.get(module_type=2)
	payload.update({
		'footer'		: footer,
		'description'	: description,
	})
	return render_to_response(tempalte_name, payload, context_instance=RequestContext(request))
