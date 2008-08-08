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