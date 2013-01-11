from django.contrib import admin
from diesel.models import (
    Competition, Team, Player, Character, Mission
)

for model in (Competition, Team, Player, Character, Mission):
    admin.site.register(model)
