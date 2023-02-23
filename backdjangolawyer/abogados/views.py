
from rest_framework import status
from rest_framework.response import Response
from .models import Abogado
from .serializers import AbogadoSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Abogado
class Lista(APIView):
    

# Create your views here.
    def get(self, *args, **kwargs):
        '''
        Lista todos los abogados en base de datos
        '''
     
        abogados= Abogado.objects.all()
        serializer = AbogadoSerializer(abogados, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
       
class listaAbodagosDetail(APIView):
    def get_specificlawyer(self,abogado_id):
        '''
        Metodo de ayuda para retornar un abogado con un id Dado
        '''
        try:
            return Abogado.objects.get(id=abogado_id)
        except Abogado.DoesNotExist:
            return None

    def put(self,request, abogado_id, *args, **kwargs):
            '''
            Actualiza un abogado por su ID
            '''
            abogado_instance = self.get_object(abogado_id)
            if not abogado_instance:
                return Response(
                    {"res":"El abogado con el id dado no existe"},
                    status = status.HTTP_400_BAD_REQUEST
                )
            
            data = {
                'title': request.data.get('autor'),
                'content': request.data.get('content'),
                'published': request.data.get('published'),
                'image': request.data.get('image'),
                'author': request.data.get('author'),
                'categories': request.data.get('categories'),
                'created': request.data.get('created'),
                'updated': request.data.get('updated')
            }

            serializer = AbogadoSerializer(instance = abogado_instance, data=data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,abogado_id, *args, **kwargs):
        '''
        Elimina un abogado con el ID dado
        '''
        abogado_instance = self.get_object(abogado_id)
        if not abogado_instance:
            return Response(
                {"res":"El abogado con el id dado no existe"},
                status = status.HTTP_400_BAD_REQUEST
            )
        abogado_instance.delete()
        return Response(
            {"res":"Object Deleted"},
            status=status.HTTP_200_OK
        )

    
        

