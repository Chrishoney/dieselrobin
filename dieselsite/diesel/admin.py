from django.contrib import admin
from diesel.models import (
    Competition, Team, Player, Character, Mission, TeamMember
)

class TeamMemberInline(admin.TabularInline):
    model=TeamMember

class TeamAdmin(admin.ModelAdmin):
    inlines = (TeamMemberInline,)

admin.site.register(Team, TeamAdmin)
admin.site.register(Player)
admin.site.register(Competition)
admin.site.register(Character)
admin.site.register(Mission)
