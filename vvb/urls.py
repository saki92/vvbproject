from django.conf.urls import patterns, include, url
from vvb.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vvb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
	(r'^home$', home),
	(r'^loggedin/$', login),
)
