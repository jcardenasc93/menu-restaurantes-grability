from django.db import models

# Create your models here.


class Restaurant(models.Model):
    """ Definición del modelo 'Restaurant'
    Se definen los siguientes campos para el modelo:
      -name: Nombre del restaurante
      -city: Ciudad de operación del restaurante (opcional)
      -address: Dirección física del restaurante o sucursal (opcional)
    """

    name = models.CharField(max_length=80, verbose_name='resturant name')
    city = models.CharField(
        max_length=50, verbose_name='restaurant city', blank=True)
    address = models.CharField(
        max_length=80, verbose_name='restaurant address', blank=True)

    class Meta:
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurants'

    def __str__(self):
        return self.name


class Product(models.Model):
    """ Definición del modelo 'Product'
    Se definen los siguientes campos para el modelo:
        -name: Nombre del producto
        -description: Descripción del producto
        -price: Precio del producto (Se asumen precios desde 0.00 a 999999.00)
    """

    name = models.CharField(max_length=120, verbose_name='product name')
    description = models.TextField(
        max_length=300, verbose_name='product description')
    price = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name='product price')
    # Relación Foreign Key al modelo Restaurant
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name='restaurant')
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
