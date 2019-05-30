from django.db import models
from django.contrib.auth.models import User # import user model

# Create your models here.

class Member(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_completo = models.CharField(max_length=50)
    sexo = models.BooleanField()
    linguagem = models.CharField(max_length=50, null=True, blank=True)
    
