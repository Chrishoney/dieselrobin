from django.shortcuts import render, redirect, get_object_or_404

from diesel.models import Team, Player, Character

def team(request, team, template='team.html'):
    team = get_object_or_404(Team, name=team)
    return render(request, template, {'team': team})

def teams(request, template='teams.html'):
    teams = Team.objects.all()
    return render(request, template, {'teams': teams})

def player(request, player, template='player.html'):
    player = get_object_or_404(Player, name=player)
    return render(request, template, {'player': player})

def players(request, template='players.html'):
    players = Player.objects.all()
    return render(request, template, {'players': players})

def character(request, character, template='characters.html'):
    character = get_object_or_404(Character, combo)
    return render(request, template, {'character': character})

def characters(request, template="characters.html"):
    characters = Character.objects.all()
    return render(request, template, {'characters': characters})

def competition(request, number, template='competition.html'):
    comp = get_object_or_404(Competition, number=number)

def standings(request, template="standings.html"):
    comp = Competition.objects.order_by('start_date')[0]
