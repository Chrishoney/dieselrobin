from django.db import models

from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length=50)
    score = models.PositiveIntegerField(default=0)

class Player(models.Model):
    name = models.CharField(max_length=20, unique=True)
    team = models.ForeignKey(Team, related_name='players')

class Character(models.Model):
    combo = models.CharField(max_length=4)
    team = models.ForeignKey(Team, related_name='characters')

class Mission(models.Model):
    pass
