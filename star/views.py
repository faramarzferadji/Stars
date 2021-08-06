from django.shortcuts import render
from django.http import HttpResponse
from .models import Player


def index(request):
    star = Player.objects.all()


    return render(request, 'index.html',
                  {'star':star})


# Create your views here.
