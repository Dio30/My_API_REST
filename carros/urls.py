from rest_framework.routers import SimpleRouter
from .views import CarrosViewSet

routers = SimpleRouter()
routers.register('carros', CarrosViewSet) # api/v1/carros