from rest_framework import serializers
from .models import CreditCard

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = '__all__'