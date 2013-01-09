from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

# cumulative stat ideas:
# missions finished
# characters killed
# total competitions
# competition wins

class Competition(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    random_teams = models.BooleanField(default=False)
    team_size = models.PositiveSmallIntegerField()

    def __unicode__(self):
        return u'%s' % self.name
    
    @property
    def ongoing(self):
        now = timezone.now()
        return (start - now).days < 0 < (end - now).days

    @property
    def name(self):
        return u'Dieselrobin %s' % self.start_date.strftime('%A %Y')


class Team(models.Model):
    '''
    Represent a team.

    Holds the team name, the team score, and a few pieces of data
    '''
    name = models.CharField(max_length=50)
    score = models.PositiveIntegerField(default=0)
    competition = models.ForeignKey(Competition, related_name='teams')

    def __unicode__(self):
        return u'%s' % self.name

    @property
    def members(self):
        return self.players.filter(team=self.name)

    @property
    def score(self):
        chars = self.characters.all()
        team_characters = chars.players.filter(team=self.id)
        total = 0
        for char in team_characters:
            total += char.points
        return u'%s' % total


class Player(models.Model):
    '''
    Represent a player.

    The ForeignKey to auth.models.User is for retrieving the player name.
    The ForeignKey to Team is for looking up players by team. There are a
    couple statistical counters for tracking player performance over time.
    '''
    # attributes
    name = models.ForeignKey(User)
    team = models.ForeignKey(
        Team, blank=True, null=True, related_name='players'
    )
    completed_missions = models.PositiveIntegerField(default=0)
    killed_characters = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return u'%s' % self.name.username


class Character(models.Model):
    '''
    Define a character and related data.

    Character has a ForeignKey to team for looking up all characters owned
    by a team. 

    '''
    # attributes
    combo = models.CharField(max_length=4)
    team = models.ForeignKey(
        Team, blank=True, null=True, related_name='characters'
    )
    chosen_by = models.ForeignKey(User)

    # tourney data
    points = models.PositiveIntegerField(default=0)
    won = models.BooleanField(default=False)

    def __unicode__(self):
        return u'<Character - %s>' % self.combo

    @property
    def alive(self):
        '''
        Return True if any mission has been failed.

        Failed and complete represent two different things.
        '''
        qs = self.regular_missions.filter(combo=self.id)
        return not any(mission.failed for mission in qs)
