from rest_framework	import serializers
from .models import Chela
##Serializador
class ChelaSerializer(serializers.ModelSerializer):
	class Meta:
		model=Chela
		fields="__all__" #serializar todos los atributos del modelo
		#Se puede serializar una cantidad de campos 
