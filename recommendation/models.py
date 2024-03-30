from django.db import models

from post.models import Post


# Create your models here.
class Recommendation(models.Model):
    texte = models.TextField()
    poste = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.texte
