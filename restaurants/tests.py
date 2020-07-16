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
        """Este test valida que el endpoint '/restaurants/' exista y que devuelva
        la cantidad correcta de restaurantes creados. Adicionalmente se valida
        el nombre de un restaurante
        """

        response = self.client.get(reverse('list_restaurants'), formal='json')
        response_data = json.loads(response.content)
        restaurant_1 = Restaurant.objects.get(name='Coma y vuelva')

        for resturant in response_data['restaurants']:
            # Busca el restaurante que coincida con el nombre definido
            if resturant['name'] == 'Coma y vuelva':
                restaurant_2 = resturant

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_data['total'], 2)
        self.assertEqual(restaurant_2['id'], restaurant_1.id)
