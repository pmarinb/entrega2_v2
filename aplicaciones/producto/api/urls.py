from rest_framework import routers
from .views import VehiculoViewSet

router =  routers.SimpleRouter()
router.register('vehiculo', VehiculoViewSet)

urlpatterns = router.urls