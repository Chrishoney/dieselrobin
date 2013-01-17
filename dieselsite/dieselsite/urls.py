from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

# separate url dispatch files are stupid. all of them are in here.

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)   

urlpatterns += patterns('info.views',
    url(r'^$', 'index', name='index'),
    url(r'^rules/$', 'rules', name='rules'),
    url(r'^bonus/$', 'bonus', name='bonus'),
    url(r'^regular/$', 'regular', name='regular'),
)

urlpatterns += patterns('diesel.views',
    url(r'^standings/$', 'standings', name='standings'),
    url(r'^players/$', 'players', name='players'),
    url(r'^players/(?P<player>\w{1,20})', 'player', name='player'),
    url(r'^teams/$', 'teams', name='teams'),
    url(r'^teams/(?P<team>[\w\s]+)/$', 'team', name='team'),
    url(r'^characters/$', 'characters', name='characters'),
    url(r'^characters/(?P<name>\w{1,20})', 'character', name='character'),
    url(r'^competition/(?P<number>\d+)/$', 'competition', name='competition'),
)
