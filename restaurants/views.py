from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Restaurant, Product
from .serializers import RestaurantSerializer, ProductsSerializer


# Create your views here.

class RestaurantsView(APIView):
    """ Vista basada en clase para manejar las peticiones
    hacia el modelo de Restaurant
    """

    def get(self, request):
        # Cuando se realiza una petición GET el API retorna todos los objetos Restaurant existentes
        restaurants = Restaurant.objects.all()
        total = restaurants.count()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response({'total': total, 'restaurants': serializer.data}, status=status.HTTP_200_OK)


class ProductsViews(APIView):
    """Vista basada en clase para manejar las peticiones
    hacia el modelo Product
    """

    def get(self, request, pk=None):
        # Cuando se realiza una petición GET el API retorna los objetos Products relacionados con el 
        # restaurante capturado desde la URL. Si el ID no existe retorna 404
        restaurant = get_object_or_404(Restaurant, id=pk)
        products = Product.objects.filter(restaurant=restaurant.id)
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
