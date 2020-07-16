from django.test import TestCase
from django.urls import reverse
import json

from .models import Restaurant
# Create your tests here.


class RestaurantsTestCase(TestCase):
    def setUp(self):
        # La configuracion inicial crea 2 restaurantes

        restaurant_1 = Restaurant.objects.create(name='Coma y vuelva')
        restaurant_2 = Restaurant.objects.create(name='Restaurante Italiano')

    def test_ListRestaurants(self):
        # Este test valida que el endpoint '/restaurants/' exista y que devuelva
        # la cantidad correcta de restaurantes creados

        response = self.client.get(reverse('list_restaurants'), formal='json')
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response_data), 2)
