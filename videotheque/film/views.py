from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Supprimer_Film, Creer_Film_Form


# Create your views here.

def liste_film(request):
    films = ['Se7en', 'Titanic', 'snatch','associé du diable', 'Retour vers le futur', 'Toy Story', 'Jurassic Park', 'Dirty Dancing']
    return render(request, 'liste_film.html', {'films': films})


def contact(request):
    return render(request, 'contact.html')


def supprimer(request):

    form = Supprimer_Film

    #faire quelque chose quand c'est GET
    if request.method == "GET":
        return render(request, 'supprimer.html', {'form' : form})


    #faire quelque chose quand c'est POST
    form_retour = Supprimer_Film(request.POST)
    if form_retour.is_valid():
        titre = form_retour.cleaned_data['titre']
        date = form_retour.cleaned_data['date_sortie']
        return HttpResponse(f'Titre : {titre} | Date : {date}')
    
    return HttpResponse("Envoyé mais formulaire incorrect")


def creation_film(request):
    if request.method == "POST":
        form = Creer_Film_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste')
        
    return render(request, 'ajout.html', {'form': Creer_Film_Form})
        
