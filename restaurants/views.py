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
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
