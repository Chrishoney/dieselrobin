from django.conf.urls import patterns, include, url

urlpatterns = patterns('diesel.views',
    url(r'^players/$', 'players', name='players'),
    url(r'^players/(?P<player>\w{1,20})', 'player', name='player'),
    url(r'^teams/$', 'teams', name='teams'),
    url(r'^teams/(?P<team>[\w\s]+)/$', 'team', name='team'),
    url(r'^characters/$', 'characters', name='characters'),
    url(r'^characters/(?P<player>\w{1,20}', 'character', name='character'),
)
