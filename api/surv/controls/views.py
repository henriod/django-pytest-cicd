from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .serializers import ControlSerializer
from .models import Control

# Create your views here.
class ControlViewset(viewsets.ModelViewSet):
    serializer_class = ControlSerializer
    queryset = Control.objects.all().order_by("-last_update")
    pagination_class = PageNumberPagination