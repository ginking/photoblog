#-*- coding: utf-8 -*-
from django.contrib import admin
from gallery.models import *

class AlbumsAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'last_edit', 'hidden')
    list_filter = ('hidden',)

class PhotosAdmin(admin.ModelAdmin):
    def filter(self):
        return '<a href="?album=%s">%s</a>' % (self.album_id, self.album)
    filter.allow_tags = True

    list_display = ('name', filter, 'created', 'like', 'not_like')
    search_fields = ('name',)

admin.site.register(Albums, AlbumsAdmin)
admin.site.register(Photos, PhotosAdmin)
