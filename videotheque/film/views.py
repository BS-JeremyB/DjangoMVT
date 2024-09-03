from django.shortcuts import render


# Create your views here.

def liste_film(request):
    films = ['Se7en', 'Titanic', 'snatch','associé du diable', 'Retour vers le futur', 'Toy Story', 'Jurassic Park', 'Dirty Dancing']
    return render(request, 'liste_film.html', {'films': films})


def contact(request):
    return render(request, 'contact.html')