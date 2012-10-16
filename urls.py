from django.conf.urls.defaults import *
from django.contrib import admin
from gallery.views import *
from django.http import HttpResponseRedirect as redirect
admin.autodiscover()
import os.path

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '/opt/photoblog/media/'}),
    (r'^$', main),
    (r'^gallery/', include('gallery.urls')),
)
