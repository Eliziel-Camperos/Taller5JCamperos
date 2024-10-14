from django.db import models # type: ignore

# Create your models here.
class Alumno(models.Model):
	apaterno =models.Charfield(max_length=50,verbose_name='Apaterno')
	amaterno =models.Charfield(max_length=50,verbose_name='Amaterno')
	nombres =models.Charfield(max_length=50,verbose_name='nombres')
	fecha_naci=models.DateField(verbose_name='fecha_nacimiento',null=False,blank=False)
	fecha_falle=models.DateField(verbose_name='fallecimiento',null=True,blank=True)
	fecha_ingre=models.DateField(verbose_name='ingreso',null=True,blank=True)

#usuario admin
#contra jujutsu