from apps.custom_user.serializers import AccountSerializer
from rest_framework import serializers
from .models import Item, Transaction


class ItemTransSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = 'id', 'name',


class ItemDetailSerializer(serializers.ModelSerializer):
    max_price = serializers.SerializerMethodField()
    income = serializers.SerializerMethodField()
    min_price = serializers.SerializerMethodField()
    mid_price = serializers.SerializerMethodField()
    quantity_percent = serializers.SerializerMethodField()
    quantity_self = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = '__all__'

    def get_max_price(self, obj):
        try:
            return obj.price + ((obj.percent * obj.price) / 100)
        except:
            return 0

    def get_min_price(self, obj):
        try:
            return obj.price + ((obj.min_percent * obj.price) / 100)
        except:
            return 0

    def get_mid_price(self, obj):
        try:
            new_percent = (obj.min_percent + obj.percent) / 2
            new_price = obj.price + ((new_percent * obj.price) / 100)
            return new_price
        except:
            return 0

    def get_income(self, obj):
        try:
            new_price = (obj.price + ((obj.percent * obj.price) / 100))
            return new_price - obj.price
        except:
            return 0

    def get_quantity_percent(self, obj):
        try:
            return (obj.price + ((obj.percent * obj.price) / 100)) * obj.count
        except:
            return 0

    def get_quantity_self(self, obj):
        try:
            return obj.price * obj.count
        except:
            return 0


class TransactionSerializer(serializers.ModelSerializer):
    items = ItemTransSerializer(many=True)
    author = AccountSerializer()

    class Meta:
        model = Transaction
        fields = '__all__'


class TransactionPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


class BuyItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "id", "name", "item", "type_in", "sum", "pub_date",