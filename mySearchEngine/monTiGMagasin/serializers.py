from rest_framework.serializers import ModelSerializer
from monTiGMagasin.models import InfoProduct
from rest_framework import serializers


class InfoProductSerializer(ModelSerializer):
    tig_id = serializers.IntegerField(required=True)
    name = serializers.CharField(required=True)
    category = serializers.IntegerField(required=True)
    price = serializers.DecimalField(required=True, max_digits=10, decimal_places=2)
    unit = serializers.CharField(required=True)
    availability = serializers.BooleanField(required=True)
    sale = serializers.BooleanField(required=True)
    discount = serializers.DecimalField(required=True, max_digits=10, decimal_places=2)
    comments = serializers.CharField(required=False)
    owner = serializers.CharField(required=True)
    quantityInStock = serializers.IntegerField(required=True)
    class Meta:
        model = InfoProduct
        fields = ('id', 'tig_id', 'name', 'category', 'price', 'unit', 'availability', 'sale', 'discount', 'comments', 'owner', 'quantityInStock')
