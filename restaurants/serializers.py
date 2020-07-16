from rest_framework import serializers
from .models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    """ Definición de la clase RestaurantSerializer
    que permite serializar el modelo 'Restaurant' para
    exponer su información a través del API en formato JSON 
    """

    class Meta:
        model = Restaurant
        fields = '__all__'
