from rest_framework import serializers
from .models import Abogado

class AbogadoSerializer(serializers.ModelSerializer):

    class Meta:
        model=Abogado
        fields='__all__'
                
                
	
	  
	      
    
   
