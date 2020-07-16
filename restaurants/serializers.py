from rest_framework import serializers
from .models import Restaurant, Product


class RestaurantSerializer(serializers.ModelSerializer):
    """ Definición de la clase RestaurantSerializer
    que permite serializar el modelo 'Restaurant' para
    exponer su información a través del API en formato JSON 
    """

    class Meta:
        model = Restaurant
        fields = '__all__'


class ProductsSerializer(serializers.ModelSerializer):
    """ Definición de la clase ProductsSerializer
    que permite serializar el modelo 'Product' para
    exponer su información a través del API en formato JSON 
    """
    restaurant = RestaurantSerializer(read_only=True)
    class Meta:
        model = Product
        fields = '__all__'