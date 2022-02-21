from rest_framework import routers
from .views import ControlViewset

control_router = routers.DefaultRouter()
control_router.register("controls", viewset=ControlViewset, basename="controls")
