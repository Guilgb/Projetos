from rest_framework import serializers
from dompizzaioloApp.models import User, Food, Order


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class ListOrderFoodsSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.name_user')
    food = serializers.ReadOnlyField(source='food.name_food')

    class Meta:
        model = Order
        fields = ['user', 'food']
