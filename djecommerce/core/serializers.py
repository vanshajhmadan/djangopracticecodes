from rest_framework import serializers
from .views import *
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'stripe_customer_id', 'one_click_purchasing']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['title', 'price', 'discount_price',
                  'category', 'label', 'slug', 'description', 'image']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['user', 'ordered', 'item', 'quantity']


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['user', 'ref_code', 'items', 'start_date', 'ordered_date', 'ordered', 'shipping_address',
                  'billing_address', 'payment', 'coupon', 'being_delivered', 'received', 'refund_requested',
                  'refund_granted']

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['stripe_charge_id','user','amount','timestamp']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['user','street_address','apartment_address','zip','address_type','default']

class RefundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refund
        fields = ['order','reason','accepted','email']
