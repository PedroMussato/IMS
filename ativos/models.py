import uuid
from django.db import models
from django.contrib.auth.models import User
from pessoal.models import Departamento


# Create your models here.
class Brand(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    brand_name = models.CharField(max_length=50)

class Classe(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=2048, null=True)

class Ativo(models.Model):
    id = models.CharField(max_length=6, unique=True, primary_key=True) # geração automatica
    item_class = models.ForeignKey(Classe, on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    item_id = models.CharField(max_length=100) # identificação do item em si
    item_model = models.CharField(max_length=100)
    especifications = models.TextField(max_length=2048, null=True)
    status = models.BooleanField() # False para em uso True para disponivel

class Pacote(models.Model):
    id = models.CharField(max_length=7, unique=True, primary_key=True) # geração automatica
    type = models.BooleanField() # False para em saida True para entrada de ativo
    open = models.BooleanField(default=True) # False para fechado True para aberto
    department = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    reason = models.CharField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class RelacionamentoPacote(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    pacote = models.ForeignKey(Pacote, on_delete=models.CASCADE, null=True)
    ativo = models.ForeignKey(Ativo, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)