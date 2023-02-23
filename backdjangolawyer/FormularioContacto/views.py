from django.shortcuts import render
from .serializers import FormularioSerializer



#Rest Imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class ContactForm(APIView):
    def post(self,request, *args, **kwargs):
        '''
        Crea un un contacto en base de datos
        '''
        data = {
           
            'name': request.data.get('name'),
            'lastname': request.data.get('lastname'),
            'gmail': request.data.get('gmail'),
            'fecha_pub': request.data.get('fecha_pub'),
            'fecha_creacion': request.data.get('fecha_pub')
        }

        serializer = FormularioSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data , status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

