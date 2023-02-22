
from rest_framework import status
from rest_framework.response import Response
from .models import Abogado
from .serializers import AbogadoSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

class Lista(APIView):
    

# Create your views here.
    def get(self, *args, **kwargs):
        abogados= Abogado.objects.all()
        serializer = AbogadoSerializer(abogados, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
       
    
        
        

