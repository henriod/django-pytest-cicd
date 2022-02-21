from django.shortcuts import render
from django.core.mail import send_mail
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination

from .serializers import ControlSerializer
from .models import Control

# Create your views here.
class ControlViewset(viewsets.ModelViewSet):
    serializer_class = ControlSerializer
    queryset = Control.objects.all().order_by("-last_update")
    pagination_class = PageNumberPagination

@api_view(http_method_names =["POST"])
def send_control_email(request:Request)->Response:
    """
    sends emails with request payload 
    sender: ford.henriod@gmail.com
    receiver: odhiambo.benard55@gmail.com
    """
    send_mail(subject=request.data.get("subject"), message=request.data.get("message"), from_email="test12django@gmail.com", recipient_list=["odhiambo.benard55@gmail.com"])
    return Response({"status":"success", "info":"email sent successfully"}, status = 200)