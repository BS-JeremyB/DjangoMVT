from django import forms
from django.forms import ModelForm
from .models import Film



class Supprimer_Film(forms.Form):
    titre = forms.CharField(max_length=150)
    date_sortie = forms.DateField(widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}))

class Creer_Film_Form(ModelForm):
    class Meta:
        model = Film
        fields = '__all__'