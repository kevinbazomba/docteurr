from django.db import models
from django.contrib.auth.models import AbstractUser

# Creation de models.


class Use(AbstractUser): # compte et enregistrement.
    pass

class Message(models.Model):
    personne = models.ForeignKey(Use, on_delete=models.CASCADE)
    message = models.TextField(blank=False)