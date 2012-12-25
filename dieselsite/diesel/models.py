from django.db import models

from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length=50)
    score = models.PositiveIntegerField(default=0)

class Player(models.Model):
    name = models.ForeignKey(User)
    team = models.ForeignKey(Team, related_name='players')

    completed_missions = models.PositiveIntegerField(default=0)
    killed_characters = models.PositiveIntegerField(default=0)

class Character(models.Model):
    combo = models.CharField(max_length=4)
    team = models.ForeignKey(Team, related_name='characters')
    alive = models.BooleanField(default=True)

class Mission(models.Model):
    player = models.ForeignKey(Player)
    combo = models.ForeignKey(Character)

    description = models.TextField()
    complete = models.BooleanField(default=False)
    failed = models.BooleanField(default=False)

    @property
    def number(self):
        return self.id
