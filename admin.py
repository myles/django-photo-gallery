"""
	Copyright (c) 2008, Myles Braithwaite
	All rights reserved.
	
	This software is provided without warranty under the terms of the BSD
	license included in photos/LICENSE.markdown and may be redistributed only under
	the conditions described in the aforementioned license. This license is also
	available online at http://code.google.com/p/django-photo-gallery/wiki/License
	
	Author: Myles Braithwaite
"""

from django.contrib import admin

from photos.models import Module, Gallery, Photo

class ModuleAdmin(admin.ModelAdmin):
	list_display = ('module_type', 'site',)

admin.site.register(Module, ModuleAdmin)

class GalleryAdmin(admin.ModelAdmin):
	list_display = ('title',)
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(Gallery, GalleryAdmin)

class PhotoAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	list_display = ('title', 'gallery', 'location', 'favorite')

admin.site.register(Photo, PhotoAdmin)