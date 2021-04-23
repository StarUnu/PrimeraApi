from django.db import models

# Create your models here.
class Chela(models.Model):
	marca=models.CharField(max_length=50)
	alcohol=models.DecimalField(max_digits=4,decimal_places=2)
	militros=models.IntegerField()
	artesanal=models.BooleanField()
	nacionalidad=models.CharField(max_length=50, blank=True, null=True)
	creado=models.DateTimeField(auto_now_add=True)
	editado=models.DateTimeField(auto_now=True)
	"""docstring for Chela"""
	def __str__(self):
		return self.marca

#se crea la tabla y despues se hace una migración automaticamente lo hace dijango
#para reflejar en la base de datos los modelos se van a convertir en tablas
#manage migrate , lo va a creer
#tan solo crear un modelo hay un crud