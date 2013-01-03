from django.db import models
from django.contrib.auth.models import User

# choice tuples
REGULAR_CHOICES = tuple((n, str(n)) for n in xrange(1, 15))
BONUS_CHOICES = tuple(REGULAR_CHOICES[:3])

class Team(models.Model):
    '''
    Represent a team.

    Holds the team name, the team score, and a few pieces of data
    '''
    name = models.CharField(max_length=50)
    score = models.PositiveIntegerField(default=0)
    max_players = models.PositiveIntegerField(default=3)

    def __unicode__(self):
        return u'<Team - %s>' % self.name

    def is_full(self):
        return self.players.all().count() == self.max_players

    def players(self):
        return self.players.filter(team=self.name)

    def score(self):
        characters = self.objects.all()
        team_characters = characters.players.filter(team=self.id)
        score = 0
        for char in team_characters:
            score += char.points
        return u'%s' % score


class Player(models.Model):
    '''
    Represent a player.

    The ForeignKey to auth.models.User is for retrieving the player name.
    The ForeignKey to Team is for looking up players by team. There are a
    couple statistical counters for tracking player performance over time.
    '''
    # attributes
    name = models.ForeignKey(User)
    team = models.ForeignKey(Team, related_name='players')

    # tourney data
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
    team = models.ForeignKey(Team, related_name='characters')
    chosen_by = models.ForeignKey(User)

    # tourney data
    points = models.PositiveIntegerField(default=0)
    alive = models.BooleanField(default=True)
    won = models.BooleanField(default=False)

    def __unicode__(self):
        return u'<Character - %s>' % self.combo


class MissionBase(models.Model):
    '''
    Abstract base class that contains data in common to both mission types
    
    This model cannot be instantiated directly, you must subclass it.
    '''
    player = models.ForeignKey(Player)
    combo = models.ForeignKey(Character)
    description = models.TextField()
    complete = models.BooleanField(default=False)

    class Meta:
        abstract = True

class RegularMission(MissionBase):
    number = models.PositiveIntegerField(choices=REGULAR_CHOICES)
    failed = models.BooleanField(default=False)
    new_locations = models.CharField(
        max_length=255, help_text="New locations allowed by this mission"
    )

    def __unicode__(self):
        return u'Mission %s' % self.number

class BonusMission(MissionBase):
    tier = models.PositiveIntegerField(choices=BONUS_CHOICES)
    number = models.PositiveIntegerField(BONUS_CHOICES)

    def __unicode__(self):
        return u'Bonus Mission: Tier %s, Mission %s' % (self.tier, self.number)
