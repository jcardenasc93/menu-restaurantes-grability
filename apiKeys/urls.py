from django.urls import path
from . import views

urlpatterns = [
    # API_KEY endpoints
    path('api-key/create', views.createAPIKey, name='create_apiKey'),

]
