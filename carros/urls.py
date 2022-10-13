from rest_framework.routers import SimpleRouter
from .views import CarrosViewSet, list_carros, post_carros, editar_carro
from django.urls import path

routers = SimpleRouter()
routers.register('carros', CarrosViewSet)

urlpatterns = [
    path('', list_carros, name='lista_carros'),
    path('novo_carro/', post_carros, name='novo_carro'),
    path('editar_carro/', editar_carro, name='editar_carro'),
]