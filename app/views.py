from django.shortcuts import render, get_object_or_404

from .models import Game 

def index(request):

    games = Game.objects.all()

    return render(request, 'index.html',{
        'games': games
    })

def connexion(request):
    return render(request, 'connexion.html')

def game(request, id):
    game = get_object_or_404(Game, id=id)
    return render(request, 'game.html', {'game': game})