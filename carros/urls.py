from rest_framework.routers import SimpleRouter
from .views import CarrosViewSet, list_carros
from django.urls import path

routers = SimpleRouter()
routers.register('carros', CarrosViewSet)

urlpatterns = [
    path('', list_carros, name='lista_carros')
]