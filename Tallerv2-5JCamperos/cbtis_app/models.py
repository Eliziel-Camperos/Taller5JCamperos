from django.db import models

# Create your models here.
class Alumno(models.Model):
	apaterno =models.Charfield(max_length=50,verbose_name='Apaterno')
