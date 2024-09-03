from django.shortcuts import render
from django.http import HttpResponse

def accueil(request):
    return HttpResponse("Bienvenue !")


def connexion(request):
    return HttpResponse("vous êtes sur la page de connexion")

# Create your views here.
