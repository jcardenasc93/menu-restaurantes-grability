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

    def get_list(self, request):
        # Cuando se realiza una petición GET el API retorna todos los objetos Restaurant existentes
        restaurants = Restaurant.objects.all()
        total = restaurants.count()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response({'total': total, 'restaurants': serializer.data}, status=status.HTTP_200_OK)


class ProductsViews(viewsets.ModelViewSet):
    """Vista basada en clase para manejar las peticiones
    hacia el modelo Product
    """

    def get_list(self, request, pk=None):
        # Cuando se realiza una petición GET el API retorna los objetos Products relacionados con el
        # restaurante capturado desde la URL. Si el ID no existe retorna 404
        restaurant = get_object_or_404(Restaurant, id=pk)
        products = Product.objects.filter(restaurant=restaurant.id)
        products_serializer = ProductsSerializer(products, many=True)
        restaurant_data = {'id': restaurant.id, 'name': restaurant.name}

        return Response({'restaurant': restaurant_data, 'total': products.count(), 'products': products_serializer.data}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        # Cuando se realiza una petición GET el servidor identifica si el ID capturado en la URL pertenece a un producto
        # de ser asi, el API retorna el detalle del producto

        product = Product.objects.get(id=pk)
        product_serializer = ProductsSerializer(product)
        restaurant_data = product.restaurant.name

        return Response({'restaurant_name': restaurant_data, 'product_detail': product_serializer.data}, status=status.HTTP_200_OK)
