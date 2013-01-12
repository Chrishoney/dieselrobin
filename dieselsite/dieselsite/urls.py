from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
) += patterns('info.views',
    # these are included here instead of in a separate file
    url(r'^rules/$', 'rules', name='rules'),
    url(r'^combos/$', 'combos', name='combos'),
    url(r'^missions/bonus/$', 'bonus', name='bonus'),
    url(r'^missions/regular/$', 'regular', name='regular'),
)
