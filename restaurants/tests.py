from django.test import TestCase
from django.urls import reverse
import json

from .models import Restaurant, Product
# Create your tests here.


class RestaurantsTestCase(TestCase):
    def setUp(self):
        # La configuracion inicial crea 2 restaurantes

        restaurant_1 = Restaurant.objects.create(name='Coma y vuelva')
        restaurant_2 = Restaurant.objects.create(name='Restaurante Italiano')

    def test_list_restaurants(self):
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


class ProductsTestCase(TestCase):
    def setUp(self):
        # La configuracion inicial crea un objeto Restaurant y agrega 5 productos
        restaurant_test = Restaurant.objects.create(name='Siempre lleno')
        for i in range(0, 5):
            Product.objects.create(
                name='Producto ' + str(i),
                description='''A continuación se describen las características del producto ofertado.
                Se debe describir su sabor, sus ingredientes de forma tal que impacten el paladar del consumidor.
                ''',
                price=5000 * 12.0 / (i + 1),
                restaurant=restaurant_test
            )

    def test_list_products(self):
        restaurant_test = Restaurant.objects.get(name='Siempre lleno')
        response = self.client.get(reverse('list_products', kwargs={
                                   'pk': restaurant_test.id}), formal='json')
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)  # Valida codigo de estado        
        self.assertEqual(len(response_data), 5) # Valida la cantidad de productos
