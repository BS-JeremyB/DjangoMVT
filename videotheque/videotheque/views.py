from django.http import HttpResponse

def accueil(request):
    return HttpResponse("Vous êtes sur l'accueil !")