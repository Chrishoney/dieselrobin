from django.contrib import admin
from diesel.models import (
    Team, Player, Character, Regular, Bonus
)

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Character)
admin.site.register(Regular)
admin.site.register(Bonus)
