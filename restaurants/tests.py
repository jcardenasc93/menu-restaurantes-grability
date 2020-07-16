from django.test import TestCase
from django.urls import reverse
import json
from decimal import Decimal
from .models import Restaurant, Product

# Create your tests here.

class RestaurantsTestCase(TestCase):
    # En esta clase serán ejecutadas las pruebas unitarias para endpoint que retorna el listado de restaurantes
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

    def test_api_key_validation(self):
        # Este test valida el acceso al endpoint 'restaurants/' por medio de un API-KEY
        response = self.client.get(reverse('list_restaurants'), formal='json')
        response_data = json.loads(response.content)

        self.assertEqual(response.status_code, 403)


class ProductsTestCase(TestCase):
    # En esta clase serán ejecutadas las pruebas unitarias para endpoint que retorna el listado de productos asociados a un restaurante
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
        products = Product.objects.filter(restaurant=restaurant_test.id)

        # Calcula la sumatoria de los precios de los productos creados
        total_products_price = 0
        for prodcut in products:
            total_products_price += prodcut.price

        response = self.client.get(reverse('list_products', kwargs={
                                   'pk': restaurant_test.id}), formal='json')
        response_data = json.loads(response.content)

        # Calcula la sumatoria de los precios de los productos consultados
        total_products_price_data = 0
        for prodcut_data in response_data['products']:
            total_products_price_data += float(prodcut_data['price'])

        self.assertEqual(response.status_code, 200)  # Valida codigo de estado
        # Valida la cantidad de productos
        self.assertEqual(response_data['total'], 5)
        self.assertEqual(response_data['restaurant']
                         ['name'], restaurant_test.name)  # Valida la cantidad de productos
        # Valida las sumatorias totales
        self.assertEqual(total_products_price, total_products_price_data)

    def test_api_key_validation(self):
        # Este test valida el acceso al endpoint 'restaurant/<int:pk>/products' por medio de un API-KEY
        restaurant_test = Restaurant.objects.get(name='Siempre lleno')
        products = Product.objects.filter(restaurant=restaurant_test.id)
        response = self.client.get(reverse('list_products', kwargs={
                                   'pk': restaurant_test.id}), formal='json')
        response_data = json.loads(response.content)

        self.assertEqual(response.status_code, 403)


class ProductDetailTestCase(TestCase):
    # En esta clase serán ejecutadas las pruebas unitarias para endpoint que retorna el detalle de un producto
    def setUp(self):
        # La configuracion inicial crea un objeto Restaurant y agrega 3 productos
        restaurant_test = Restaurant.objects.create(
            name='Arroz con Habichuela')
        for i in range(0, 3):
            Product.objects.create(
                name='Producto ' + str(i),
                description='''A continuación se describen las características del producto ofertado.
                Se debe describir su sabor, sus ingredientes de forma tal que impacten el paladar del consumidor.
                ''',
                price=5000 * 12.0 / (i + 1),
                restaurant=restaurant_test
            )

    def test_retrieve_product(self):
        restaurant_test = Restaurant.objects.get(name='Arroz con Habichuela')
        product_test = Product.objects.filter(
            restaurant=restaurant_test.id).first()

        # Realiza la peticion enviando el pk del primer producto creado
        response = self.client.get(reverse('product_detail', kwargs={
                                   'pk': product_test.id}), formal='json')
        self.assertEqual(response.status_code, 200)  # Valida codigo de estado

        response_data = json.loads(response.content)
        
        self.assertEqual(product_test.name,
                         response_data['product_detail']['name']) # Valida el nombre del producto retornado
        
        self.assertEqual(
            product_test.id, response_data['product_detail']['id']) # Valida el ID del producto retornado
        
        self.assertEqual(str(product_test.price),
                         response_data['product_detail']['price']) # Valida el precio del producto retornado

    def test_api_key_validation(self):
        # Este test valida el acceso al endpoint 'products/<int:pk>' por medio de un API-KEY
        restaurant_test = Restaurant.objects.get(name='Arroz con Habichuela')
        product_test = Product.objects.filter(
            restaurant=restaurant_test.id).first()
        response = self.client.get(reverse('product_detail', kwargs={
                                   'pk': product_test.id}), formal='json')
        response_data = json.loads(response.content)

        self.assertEqual(response.status_code, 403)
