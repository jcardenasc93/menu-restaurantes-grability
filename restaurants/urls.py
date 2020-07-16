from django.urls import include, path
from django.conf.urls import url
from . import views

urlpatterns = [
    # RESTAURANTS endpoints
    path('restaurants', views.RestaurantsView.as_view({'get': 'get_list'}), name='list_restaurants'),

    # PRODUCTS endpoints
    path('restaurant/<int:pk>/products', views.ProductsViews.as_view({'get': 'get_list'}), name='list_products'),
    path('product/<int:pk>', views.ProductsViews.as_view({'get': 'retrieve'}), name='product_detail'),

]
