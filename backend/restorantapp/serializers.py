from rest_framework import serializers

from .models import Menu, Order

class MenuSerializer(serializers.ModelSerializer):
    
    class Meta:
        model: Menu
        fields = ['name','price','created','updated','id']
        read_only_fields = ['created', 'updated', 'id']
    
class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model: Order
        fields = ['menu','quantity','created','updated','id']
        read_only_fields = ['created', 'updated', 'id']

