from django.db import models

from accounts.models import User

# Create your models here.
TYPE_CHOICES = (
    ('0', 'Offre'),
    ('1', 'Demande')
)


class Post(models.Model):
    image = models.ImageField(upload_to='poste/%Y/%m/%d', blank=True)
    type = models.CharField(max_length=80, choices=TYPE_CHOICES)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.type + ' - ' + str(self.id)


class Reaction(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    like = models.BooleanField(default=False)

    def __str__(self):
        return self.post.__str__() + ' by ' + self.user.__str__()
