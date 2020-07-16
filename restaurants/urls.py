from django.urls import include, path
from django.conf.urls import url
from . import views

urlpatterns = [
    # RESTAURANTS
    path('restaurants/', views.RestaurantsView.as_view(), name='list_restaurants'),
]
