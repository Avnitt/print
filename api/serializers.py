import PyPDF2
from rest_framework import serializers

from .models import Order, File


class FileS(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['pdf', 'order']


class GetOrderS(serializers.ModelSerializer):
    files = FileS(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['name', 'phone', 'block', 'service_type', 'option', 'day', 'time', 'note', 'files', 'amount']


class CreateOrderS(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['name', 'phone', 'block', 'service_type', 'option', 'day', 'time', 'note']
