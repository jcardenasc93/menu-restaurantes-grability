import factory
from factory.django import DjangoModelFactory
import random
from decimal import Decimal

from .models import Restaurant, Product


class RestaurantFactory(DjangoModelFactory):
    ''' Esta clase se define para crear objetos Restaurant implementando la librería Faker    
    y así poblar la base de datos para realizar pruebas funcionales
    '''

    class Meta:
        model = Restaurant

    name = factory.Faker('name')
    city = factory.Faker('city')
    address = factory.Faker('address')


class ProductFactory(DjangoModelFactory):
    ''' Esta clase se define para crear objetos Restaurant implementando la librería Faker    
    y así poblar la base de datos para realizar pruebas funcionales
    '''

    class Meta:
        model = Product

    name = factory.Faker('sentence')
    description = factory.Faker('text')
    price = float(Decimal(random.randrange(3500, 135000)))
