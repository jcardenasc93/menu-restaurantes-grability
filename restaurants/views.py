from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Restaurant, Product
from .serializers import RestaurantSerializer, ProductsSerializer


# Create your views here.

class RestaurantsView(viewsets.ModelViewSet):
    """ Vista basada en clase para manejar las peticiones
    hacia el modelo de Restaurant
    """
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        # Cuando se realiza una petición GET el API retorna todos los objetos Restaurant existentes
        return Restaurant.objects.all()


class ProductsViews(viewsets.ModelViewSet):
    """Vista basada en clase para manejar las peticiones
    hacia el modelo Product
    """
    serializer_class = ProductsSerializer

    def get_queryset(self, *args, **kwargs):
        # Captura el pk pasado en la URL
        pk = self.kwargs['pk']
        restaurant = get_object_or_404(Restaurant, id=pk)

        return Product.objects.filter(restaurant=restaurant.id)

    def retrieve(self, request, pk=None):
        # Cuando se realiza una petición GET el servidor identifica si el ID capturado en la URL pertenece a un producto
        # de ser asi, el API retorna el detalle del producto

        product = Product.objects.get(id=pk)
        product_serializer = ProductsSerializer(product)
        restaurant_data = product.restaurant.name

        return Response({'product_detail': product_serializer.data}, status=status.HTTP_200_OK)
