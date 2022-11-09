from rest_framework import viewsets
from .models import Carros
from .serializer import CarrosSerializer

class CarrosViewSet(viewsets.ModelViewSet):
    """
    API para fazer um CRUD completo de carros simulando uma conssessionária.
    """
    queryset = Carros.objects.all()
    serializer_class = CarrosSerializer