from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

from crawl.utils import server_data

# cumulative stat ideas:
# missions finished
# characters killed
# total competitions
# competition wins

# choice drop downs
SERVERS = tuple((name, name) for name in server_data.keys())
MISSION_TYPES = (('regular', 'Regular'), ('bonus', 'Bonus'))
REGULAR_MISSIONS = tuple((n, str(n)) for n in xrange(1, 15))
BONUS_TIERS = tuple((n, str(n)) for n in xrange(1, 4))
BONUS_LETTERS = tuple((c, c) for c in ('A', 'B', 'C'))


class Competition(models.Model):
    number = models.PositiveIntegerField()
    registration_date = models.DateTimeField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    random_teams = models.BooleanField(default=False)
    team_size = models.PositiveSmallIntegerField(default=3)

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
    '''
    related setting in common.py: 'AUTH_PROFILE_MODULE'
    '''
    user = models.OneToOneField(User)
    preferred_server = models.CharField(max_length=4, choices=SERVERS)

    def __unicode__(self):
        return u'%s' % self.user.username

    @property
    def crawl_name(self):
        return self.user.username


class Team(models.Model):
    name = models.CharField(max_length=50)
    competition = models.ForeignKey(Competition, related_name='teams')
    players = models.ManyToManyField(Player, through='TeamMember')
    server = models.CharField(max_length=4, choices=SERVERS)

    def __unicode__(self):
        return u'%s' % self.name


class TeamMember(models.Model):
    player = models.ForeignKey(Player)
    # set default foreignkey to TEAM RANDOM
    team = models.ForeignKey(Team)
    # limit play order position choices to valid ones
    position = models.PositiveSmallIntegerField(blank=True)


class Character(models.Model):
    # pre registration fields
    combo = models.CharField(max_length=4)
    picked_by = models.ForeignKey(Player, related_name='picks')
    # team related fields
    team = models.ManyToManyField(
        Team, through='TeamCharacter', blank=True,null=True
    )
    account = models.CharField(max_length=20)
    won = models.BooleanField(default=False)
    dead = models.BooleanField(default=False)

    def __unicode__(self):
        if self.account:
            return u'%s - %s' % (self.combo, self.account) 
        return u'%s' % self.combo

class TeamCharacter(models.Model):
    team = models.ForeignKey(Team)
    character = models.ForeignKey(Character)
    starting_player = models.PositiveSmallIntegerField(blank=True)


class Mission(models.Model):
    # data stored in fixtures
    type = models.CharField(max_length=7, choices=MISSION_TYPES)
    identifier = models.CharField(max_length=1)
    description = models.TextField()
    # Bonus Missions only
    tier = models.PositiveSmallIntegerField(blank=True, choices=BONUS_TIERS)

    # data assigned when a mission instance is saved.
    player = models.ForeignKey(Player, related_name='missions')
    character = models.ForeignKey(Character, related_name='missions')
    # booleans/competition related data
    player_note = models.TextField(blank=True)
    started = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
