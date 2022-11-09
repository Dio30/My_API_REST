from django.contrib import admin
from django.urls import path, include
from carros.urls import routers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(routers.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
