from django.shortcuts import render
from django.core.mail import send_mail
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination

from controls.serializers import ControlSerializer
from controls.models import Control

# Create your views here.
class ControlViewset(viewsets.ModelViewSet):
    serializer_class = ControlSerializer
    queryset = Control.objects.all().order_by("-last_update")
    pagination_class = PageNumberPagination


@api_view(http_method_names=["POST"])
def send_control_email(request: Request) -> Response:
    """
    sends emails with request payload
    sender: ford.henriod@gmail.com
    receiver: odhiambo.benard55@gmail.com
    """
    send_mail(
        subject=request.data.get("subject"),
        message=request.data.get("message"),
        from_email="test12django@gmail.com",
        recipient_list=["odhiambo.benard55@gmail.com"],
    )
    return Response(
        {"status": "success", "info": "email sent successfully"}, status=200
    )

def fibonacii_dynamic_v2(n: int) -> int:
    fib_1, fib_2 = 0, 1

    for i in range(1, n + 1):
        fi = fib_1 + fib_2
        fib_1, fib_2 = fib_2, fi

    return fib_1

@api_view(http_method_names=["POST"])
def nth_fibonaccii_number(request:Request)-> Response:
    n = request.data.get("fibonacci")
    if n == None or int(n) < 0 :
        return Response(
            {"status":"failed", "infor":f"n'th:{n} must be positive interger number"},
            status=406
        )
    
    else:
        result = fibonacii_dynamic_v2(int(n))
        return Response(
            {"status":"success", "infor":f"the n'th fibonacci number is :{result} "}
        )
