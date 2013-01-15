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
    preferred_server = models.CharField(max_length=3, choices=SERVERS)
    def __unicode__(self):
        return u'%s' % self.user.username


class Team(models.Model):
    name = models.CharField(max_length=50)
    competition = models.ForeignKey(Competition, related_name='teams')
    players = models.ManyToManyField(Player, through='TeamMember')
    server = models.CharField(max_length=4, choices=SERVERS)


class TeamMember(models.Model):
    player = models.ForeignKey(Player)
    # set default foreignkey to TEAM RANDOM
    team = models.ForeignKey(Team)
    # limit play order position choices to valid ones
    position = models.PositiveSmallIntegerField(blank=True)


class Character(models.Model):
    chosen_by = models.ForeignKey(Player, related_name='choices')
    combo = models.CharField(max_length=4)

    initial_player = models.ForeignKey(
        Player, null=True, blank=True, related_name='starts'
    )
    team = models.ForeignKey(
        Team, related_name='characters', null=True, blank=True
    )
    account = models.CharField(max_length=20, blank=True)

    won = models.BooleanField(default=False)
    dead = models.BooleanField(default=False)

    def __unicode__(self):
        return u'Team %s - %s>' % self.combo


class Mission(models.Model):
    note = models.TextField(blank=True)
    player = models.ForeignKey(Player, related_name='missions')
    character = models.ForeignKey(Character, related_name='missions')
    type = models.CharField(max_length=7, choices=MISSION_TYPES)
    number = models.PositiveSmallIntegerField(choices=REGULAR_MISSIONS)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    failed = models.BooleanField(default=False)
    # Bonus Missions only
    tier = models.PositiveSmallIntegerField(blank=True, choices=BONUS_TIERS)
    letter = models.CharField(max_length=1, blank=True, choices=BONUS_LETTERS)
