from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

from diesel.utils import SERVER_NAMES

# cumulative stat ideas:
# missions finished
# characters killed
# total competitions
# competition wins

# choice drop downs
SERVERS = tuple((name, name) for name in SERVER_NAMES)
MISSION_TYPES = (('regular', 'Regular'), ('bonus', 'Bonus'))
REGULAR_MISSIONS = tuple((n, str(n)) for n in xrange(1, 15))
BONUS_MISSIONS = tuple((n, str(n)) for n in xrange(1, 4))

class Competition(models.Model):
    registration_date = models.DateTimeField()
    end_date = models.DateTimeField()
    random_teams = models.BooleanField(default=False)
    team_size = models.PositiveSmallIntegerField(default=3)
    #players = models.ManyToManyField()

    def __unicode__(self):
        return u'%s' % self.name
    
    @property
    def ongoing(self):
        now = timezone.now()
        return (start - now).days < 0 <= (end - now).days

    @property
    def name(self):
        return u'Dieselrobin %s' % self.start_date.strftime('%A %Y')


class Player(models.Model):
    user = models.ForeignKey(User)
    next = models.ForeignKey('Player', blank=True, null=True)
    server = models.CharField(max_length=4, choices=SERVERS)
    choice = models.ManyToManyField('Character', related_name='choices')
    starting_combo = models.ManyToManyField('Character')

    def __unicode__(self):
        return u'%s' % self.user.username


class Character(models.Model):
    combo = models.CharField(max_length=4)
    account = models.CharField(max_length=20)
    won = models.BooleanField(default=False)
    dead = models.BooleanField(default=False)
    def __unicode__(self):
        return u'Team %s - %s>' % self.combo


class Mission(models.Model):
    character = models.ForeignKey(Character, related_name='missions')
    type = models.CharField(max_length=7, choices=MISSION_TYPES)
    description = models.TextField()
    complete = models.BooleanField(default=False)       
    failed = models.BooleanField(default=False)
    tier = models.PositiveSmallIntegerField(choices=BONUS_MISSIONS)
    number = models.PositiveSmallIntegerField(choices=REGULAR_MISSIONS)
