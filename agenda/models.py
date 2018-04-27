from django.db import models
from django.utils import timezone

class Pessoa (models.Model):
    nome = models.CharField('Nome', max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False , null=False)
    senha = models.CharField(max_length=20, blank=False, null=False)
    user_name = models.CharField('Nome de Usuario', max_length=50, blank=False, null=False)
    biografia = models.TextField()


