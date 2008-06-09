import os
from PIL import Image

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import permalink
from django.contrib.auth.models import User

from blog.managers import *

class Gallery(models.Model):
	"""
	Gallery model.
	"""
	title		= models.CharField(_('title'), max_length=100)
	slug		= models.SlugField(_('slug'), prepopulate_from=('title',), unique=True)
	description	= models.TextField(_('description'), blank=True, null=True)
	created		= models.DateTimeField(_('created'), auto_now_add=True)
	modified	= models.DateTimeField(_('modified'), auto_now=True)
	
	class Meta:
		verbose_name		= _('gallery')
		verbose_name_plural	= _('galleries')
		db_table			= 'photo_galleries'
		ordering			= 'title'
	
	class Admin:
		list_display	= ('title',)
	
	def __unicode__(self):
		return u"%s" % self.title
	
	@permalink
	def get_absolute_url(self):
	  	return ('photo_gallery_detail', None, {
			'slug'	: self.slug
		})

class Photo(models.Model):
	"""
	Photo model.
	"""
	title		= models.CharField(_('title'), max_length=200)
	slug		= models.SlugField(_('slug'), prepopulate_from=('title',), unique=True)
	location	= models.CharField(_('location'), max_length=50 blank=True, null=True)
	description	= models.TextField(_('description'), blank=True, null=True)
	gallery		= models.ForeignKey(Gallery)
	favorite	= models.BooleanField(_('favorite'), default=False)
	
	original	= models.ImageField(_('original'), upload_to='photos/o/%Y-%m-%d')
	large		= models.ImageField(_('large'), upload_to='photos/l/%Y-%m-%d',  editable=False)
	thumbnail		= models.ImageField(_('thumbnail'), upload_to='photos/t/%Y-%m-%d',  editable=False)
	
	created		= models.DateTimeField(_('created'), auto_now_add=True)
	modified	= models.DateTimeField(_('modified'), auto_now=True)
	
	class Meta:
		verbose_name		= _('photo')
		verbose_name_plural	= _('photos')
		db_table			= 'photos'
		ordering			= ('modified',)
	
	class Admin:
		list_display	= ('title', 'gallery', 'location', 'favorite')
	
	def __unicode__(self):
		return u"%s" % self.title
	
	@permalink
	def get_absolute_url(self):
		return ('photo_detail', None, {
			'slug'		: self.slug,
		})
	
	def save(self):
		"""
		We use PIL's Image object
		Docs: http://www.pythonware.com/library/pil/handbook/image.htm
		"""
		