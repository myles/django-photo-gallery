"""
	Copyright (c) 2008, Myles Braithwaite
	All rights reserved.
	
	This software is provided without warranty under the terms of the BSD
	license included in photos/LICENSE.txt and may be redistributed only under
	the conditions described in the aforementioned license. This license is also
	available online at http://code.google.com/p/django-photo-gallery/wiki/License
	
	Author: Myles Braithwaite
"""

import os
from PIL import Image

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import permalink
from django.contrib.auth.models import User
from django.contrib.sites.models import Site

from photos.managers import *

class Module(models.Model):
	"""
	Photo gallery site.
	"""
	MODULE_TYPE_CHOICES = (
		(1, 'Footer'),
		(2, 'Description'),
	)
	site		= models.ForeignKey(Site)
	module_type	= models.IntegerField(_('module type'), choices=MODULE_TYPE_CHOICES)
	body		= models.TextField(_('body'), help_text=_("Use Raw HTML"))
	
	class Meta:
		verbose_name		= _('module')
		verbose_name_plural	= _('modules')
		db_table			= 'photo_modules'
		ordering			= ('module_type', 'site',)
	
	class Admin:
		list_display	= ('module_type', 'site',)
	
	def __unicode__(self):
		return "%s - %s" % (self.site, self.module_type)

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
		ordering			= ('title',)
	
	class Admin:
		list_display	= ('title',)
	
	def __unicode__(self):
		return u"%s" % self.title
	
	@permalink
	def get_absolute_url(self):
	  	return ('photo_gallery_title', None, {
			'slug'	: self.slug
		})
	
	@permalink
	def get_gallery_url(self):
		return ('photo_gallery_detail', None, {
			'slug'	: self.slug
		})

class Photo(models.Model):
	"""
	Photo model.
	"""
	title		= models.CharField(_('title'), max_length=200)
	slug		= models.SlugField(_('slug'), prepopulate_from=('title',), unique=True)
	location	= models.CharField(_('location'), max_length=50, blank=True, null=True)
	description	= models.TextField(_('description'), blank=True, null=True)
	gallery		= models.ForeignKey(Gallery)
	favorite	= models.BooleanField(_('favorite'), default=False)
	
	original	= models.ImageField(_('original'), upload_to='photos/o/%Y-%m-%d')
	large		= models.ImageField(_('large'), upload_to='photos/l/%Y-%m-%d',  editable=False) # Image size no greater than 480x480
	small		= models.ImageField(_('small'), upload_to='photos/s/%Y-%m-%d',  editable=False) # Image size no greater than 90x90
	
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
			'photo_slug'	: self.slug,
			'gallery_slug'	: self.gallery.slug,
		})
	
	def save(self):
		"""
		We use PIL's Image object
		Docs: http://www.pythonware.com/library/pil/handbook/image.htm
		"""
		