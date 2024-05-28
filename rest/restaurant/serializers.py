import io
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from .models import CustomUser, Table, Category, Book, OrderItem, Order, Payment, Food, OrderItemCook


class FoodSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    category = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Category.objects.all()
    )
    class Meta:
        model = Food
        fields = "__all__"


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("username", "phone", "passport_id", 'role', "name", 'surname', 'email', 'password')


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = "__all__"


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    table = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Table.objects.all()
    )
    class Meta:
        model = Book
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    employee = serializers.SlugRelatedField(
        slug_field='username',
        queryset=CustomUser.objects.all()
    )

    class Meta:
        model = Order
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    food = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Food.objects.all()
    )
    class Meta:
        model = OrderItem
        fields = "__all__"

class OrderItemCookSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItemCook
        fields = "__all__"

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
