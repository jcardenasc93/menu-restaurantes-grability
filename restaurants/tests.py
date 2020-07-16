from django.test import TestCase
import json

from .models import Restaurant
# Create your tests here.

class RestaurantsTestCase(TestCase):
    def setUp(self):
        restaurant_1 = Restaurant.objects.create(name='Coma y vuelva')
        restaurant_2 = Restaurant.objects.create(name='Restaurante Italiano')
    
    def test_ListRestaurants(self):
        response = self.client.get('/restaurants/')
        self.assertEqual(response.status_code, 200)

