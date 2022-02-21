from rest_framework import routers
from controls.views import ControlViewset

control_router = routers.DefaultRouter()
control_router.register("controls", viewset=ControlViewset, basename="controls")
