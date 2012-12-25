from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    name = models.CharField(max_length=50)
    score = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return u'<Team - %s>' % self.name

    def players(self):
        return self.players.filter(team=self.name)


class Player(models.Model):
    name = models.ForeignKey(User)
    team = models.ForeignKey(Team, related_name='players')

    completed_missions = models.PositiveIntegerField(default=0)
    killed_characters = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return u'%s' % self.name.username

class Character(models.Model):
    # data
    combo = models.CharField(max_length=4)
    team = models.ForeignKey(Team, related_name='characters')
    points = models.PositiveIntegerField(default=0)
    # flags
    alive = models.BooleanField(default=True)
    won = models.BooleanField(default=False)

    def __unicode__(self):
        return u'<Character - %s>' % self.combo

class Mission(models.Model):
    player = models.ForeignKey(Player)
    combo = models.ForeignKey(Character)

    description = models.TextField()
    new_locations = models.CharField(
        max_length=255, help_text="New locations allowed by this mission"
    )
    complete = models.BooleanField(default=False)
    failed = models.BooleanField(default=False)

    def __unicode__(self):
        return u'<Mission %s>' % self.id

    @property
    def number(self):
        return self.id

    @property
    def short_name(self):
        return u'%s %s' % ('Mission', self.number)
