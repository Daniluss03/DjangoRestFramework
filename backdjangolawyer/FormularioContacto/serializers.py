from rest_framework import serializers
from .models import FormularioContacto


class FormularioSerializer(serializers.ModelSerializer):
    class Meta:
        model=FormularioContacto
        fields='__all__'