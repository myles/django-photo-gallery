urlpatterns = ('',
	(r'^comments/',
		view	= 'photos.views.photo_gallery_comments',
		name	= 'photo_gallery_comment',
	),
	(r'^galleries/',
		view	= 'photos.views.photo_gallery_archive',
		name	= 'photo_gallery_archive',
	),
	(r'^(?P<gallery_slug>[-\w]+)/gallery/(?P<photo_slug>[-\w]+)/',
		view	= 'photos.views.photo_gallery_photo_detail',
		name	= 'photo_gallery_photo_detail',
	),
	(r'^(?P<gallery_slug>[-\w]+)/gallery/',
		view	= 'photos.views.photo_gallery_detail',
		name	= 'photo_gallery_detail',
	),
	(r'^(?P<gallery_slug>[-\w]+)/',
		view	= 'photos.views.photo_gallery_title',
		name	= 'photo_gallery_title'
	),
	(r'^$', 
		view	= 'photos.views.gallery_index',
		name	= 'photo_gallery_index',
	),
)