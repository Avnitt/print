from rest_framework import serializers

from .models import Order, File


class FileS(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'


class GetOrderS(serializers.ModelSerializer):
    files = FileS(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['name', 'phone', 'block', 'service_type', 'option', 'day', 'time', 'note', 'files']


class CreateOrderS(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['name', 'phone', 'block', 'service_type', 'option', 'day', 'time', 'note']


    def update(self, instance, validated_data):
        # Add code for verifying the payment using gateway methods and updating the extra gateway fields
        pass
