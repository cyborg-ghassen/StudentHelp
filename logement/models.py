from django.db import models

from post.models import Post


# Create your models here.
class Logement(models.Model):
    localisation = models.CharField(max_length=100)
    description = models.TextField()
    contactinfo = models.CharField(max_length=100)
    poste = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.localisation
