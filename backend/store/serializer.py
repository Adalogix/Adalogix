from rest_framework import serializers
from .models import Store


class StoreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'name', 'capacity', 'address', 'latitude', 'longitude']
