from django.conf.urls import patterns, include, url

urlpatterns = patterns('diesel.views',
    url(r'^standings/$', 'standings', name='standings'),
    url(r'^players/$', 'players', name='players'),
    url(r'^players/(?P<player>\w{1,20})', 'player', name='player'),
    url(r'^teams/$', 'teams', name='teams'),
    url(r'^teams/(?P<team>[\w\s]+)/$', 'team', name='team'),
    url(r'^characters/$', 'characters', name='characters'),
    url(r'^characters/(?P<name>\w{1,20})', 'character', name='character'),
    url(r'^competition/(?P<number>\d+)/$', 'competition', name='competition'),
)
