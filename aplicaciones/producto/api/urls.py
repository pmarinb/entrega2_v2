from rest_framework import routers
from .views import VehiculoViewSet
from django.urls import path, include

router =  routers.SimpleRouter()
router.register('vehiculo', VehiculoViewSet)

urlpatterns = router.urls + [
    path('', include('rest_framework.urls')),
]