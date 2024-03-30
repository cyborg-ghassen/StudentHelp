from django.db import models

from post.models import Post

# Create your models here.
TYPES_CHOICES = (
    ('1', 'Ouvrier'),
    ('2', 'Technicien'),
    ('3', 'PFE'),
)


class Stage(models.Model):
    type = models.CharField(max_length=80, choices=TYPES_CHOICES)
    societe = models.CharField(max_length=100)
    duration = models.DurationField()
    sujet = models.CharField(max_length=100)
    contactinfo = models.CharField(max_length=80)
    specialite = models.CharField(max_length=100)
    poste = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.get_type_display()
