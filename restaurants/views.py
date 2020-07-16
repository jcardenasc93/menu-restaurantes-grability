from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


# Create your views here.

class RestaurantsView(APIView):
    """ Vista basada en clase para manejar las peticiones
    hacia el modelo de Restaurant
    """
    def get(self, request):
        return Response({"detail": "GET request working"}, status=status.HTTP_200_OK)
