from rest_framework import serializers
from index.models import Product


class ProductSerializer(serializers.ModelSerializer):
    category_id = serializers.StringRelatedField()
    responsible_id = serializers.StringRelatedField()
    model_id = serializers.StringRelatedField()
    class Meta:
        model = Product
        fields = ['id', 'category_id', 'responsible_id', 'model_id', 'room_number', 'qr_code']