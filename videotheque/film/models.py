from django.db import models

# Create your models here.

class Realisateur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField(null=True)
    recompense = models.IntegerField()

    def __str__(self):
        return f'{self.prenom} {self.nom}'

class Film(models.Model):
    titre = models.CharField(max_length=150)
    description = models.TextField()
    sortie = models.DateField()
    realisateur = models.ForeignKey(Realisateur, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} | {self.titre} ({self.sortie})'
