from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = {'phone', 'email', 'password', 'address', 'activated'}
        extra_kwargs = {'password': {'write_only': True}}


        def create(validated_data):
            customer = Customer.objects.create(validated_data['phone'],validated_data['password'])
            return customer

