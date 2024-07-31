from rest_framework.schemas.coreapi import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from .models import Order
from .serializers import GetOrderS

class GetOrder(APIView):
    def get_object(self, uuid):
        try:
            return Order.objects.get(uuid=uuid)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, uuid=None):
        obj = self.get_object(uuid)
        obj.count_amount()
        serializer = GetOrderS(obj)
        return Response(serializer.data)
