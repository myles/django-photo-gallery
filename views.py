from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from photos.models import Gallery, Photo, Module

def gallery_index(request):
	galleries = Gallery.objects.all()[:6]
	favorites = Photo.objects.filter(favorite=True)[:6]
	galleries_count = Gallery.objects.all().count()
	photos_count = Photo.objects.all().count()
	
	return render(request=request, template_name='photos/gallery_index.html', payload={
		'galleries': 		galleries,
		'favorites': 		favorites,
		'galleries_count':	galleries_count,
		'photos_count':		photos_count,
	})

def gallery_title(request, gallery_slug):
	gallery = get_object_or_404(Gallery, slug__iexact=gallery_slug)
	
	return render(request, 'photos/gallery_title.html', { 'gallery': gallery })

def gallery_detail(request, gallery_slug):
	gallery = get_object_or_404(Gallery, slug__iexact=gallery_slug)
	photos = Photo.objects.filter(gallery=gallery)[:25]
	
	return render(request, 'photos/gallery_detail.html', { 'gallery': gallery, 'photos': photos })

def gallery_archive(request):
	galleries = Gallery.objects.all()
	
	return render(request=request, template_name='photos/gallery_archive.html', payload={
		'galleries':	galleries,
	})

def render(request, template_name, payload):
	footer = Module.objects.get(module_type=1)
	description = Module.objects.get(module_type=2)
	payload.update({
		'footer'		: footer,
		'description'	: description,
	})
	return render_to_response(template_name, payload, context_instance=RequestContext(request))
