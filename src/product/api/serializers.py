
from rest_framework import serializers

from product.models import Product,ProductImage,ProductVariantPrice



class ProductImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('file_path',)


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        return super().create(validated_data)