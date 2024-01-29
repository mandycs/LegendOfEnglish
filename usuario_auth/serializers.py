from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'date_of_birth']  # Lista de campos que quieres incluir
        # Puedes añadir más configuraciones aquí según sea necesario
