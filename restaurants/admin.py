from django.contrib import admin
from .models import Restaurant, Product

# Register your models here.
restaurants_models = [Restaurant, Product,]
admin.site.register(restaurants_models)
