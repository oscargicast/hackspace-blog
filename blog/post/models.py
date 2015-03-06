from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    autor = models.ForeignKey(User)
    titulo = models.CharField(max_length=100)
    cuerpo = models.TextField()
