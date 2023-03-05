from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from customers.models import Customer
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        token['username'] = user.email
        print(user)
        return token


class RegisterSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=Customer.objects.all())]
    )
    password = serializers.CharField(write_only=True,required=True,validators=[validate_password])

    class Meta:
        model = Customer
        fields = ('phone', 'password')
        extra_kwargs = {
            'phone': {'required': True}
        }

    def create(self, validated_data):
        customer = Customer.objects.create(
            phone=validated_data['phone'],
            password=validated_data['password']
        )

        customer.save()
        return customer
