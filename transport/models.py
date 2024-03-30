from django.db import models

from post.models import Post


# Create your models here.
class Transport(models.Model):
    depart = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    heure_depart = models.TimeField()
    nbre_siege = models.IntegerField()
    contactinfo = models.CharField(max_length=100)
    poste = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.depart
