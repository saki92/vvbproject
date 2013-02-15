from django.conf.urls import patterns, include, url
from django.conf import settings
from vvb.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vvb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/doc', include('django.contrib.admindocs.urls')),
	(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
	(r'^home/$', home),
	(r'^loggedin/$', login),
	(r'^test/$', test),
	(r'^ref/$', refresh),
	(r'^ldname/$', ldname),
)
