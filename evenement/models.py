from django.db import models

from post.models import Post


# Create your models here.
class Event(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    lieu = models.TextField()
    contactinfo = models.TextField()
    poste = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre


class EventClub(models.Model):
    club = models.CharField(max_length=100)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.club


class EventSocial(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    prix = models.FloatField(default=0)

    def __str__(self):
        return self.prix
