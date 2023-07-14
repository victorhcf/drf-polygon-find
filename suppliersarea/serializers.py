from rest_framework import serializers
from suppliersarea.models import Provider, ServiceArea


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ['id', 'name', 'email', 'phonenumber', 'currency']


class ServiceAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceArea
        fields = ['id', 'name', 'price', 'provider', 'information']