from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)   

urlpatterns += patterns('info.views',
    url(r'^rules/$', 'rules', name='rules'),
    url(r'^missions/bonus/$', 'bonus', name='bonus'),
    url(r'^missions/regular/$', 'regular', name='regular'),
)
