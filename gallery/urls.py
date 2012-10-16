from django.conf.urls.defaults import *
from django.contrib import admin
from gallery.views import *
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', browser),
    (r'^(?P<img_id>\d+)/$', photo),
    (r'^title_by_id/(?P<img_id>\d+)/$', title_by_id),
    (r'^content_by_id/(?P<img_id>\d+)/$', content_by_id)
)
