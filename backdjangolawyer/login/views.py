from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import loginSerializer
from rest_framework import status
# Create your views here.
@api_view(['GET'])
def user_View(request):
    serializer=loginSerializer(request.user)
    return Response(serializer.data,status=status.HTTP_200_OK)