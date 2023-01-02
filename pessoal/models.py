from django.contrib.auth.models import User
from django.db import models
import uuid


# Create your models here.
class Departamento(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=50)

class RelColabDpto(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    dpto = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
