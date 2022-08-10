from carro.models import OrderItem, Order
from rest_framework import serializers
from productos.API.serializers import ProductoSerializer


class MyOrderItemSerializer(serializers.ModelSerializer):
    product = ProductoSerializer()

    class Meta:
        model = OrderItem
        fields = "__all__"



class MyOrderSerializer(serializers.ModelSerializer):
    items = MyOrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = "__all__"


    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)

        return order