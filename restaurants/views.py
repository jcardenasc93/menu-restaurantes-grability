from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import Restaurant
from .serializers import RestaurantSerializer


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

    def get(self, request):
        # Devuelve un mensaje que valida la peticion
        return Response({'detail': 'GET request valid'}, status=status.HTTP_200_OK)

