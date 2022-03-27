from rest_framework import serializers
from order.models import Shop, Order, Menu, OrderFood

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu 
        fields = '__all__'