from rest_framework import serializers

from product.models import Product, ProductImage, ProductVariantPrice


class VariantSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductVariantPrice
        fields = '__all__'


class ProductImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('file_path',)


class ProductModelSerializer(serializers.ModelSerializer):
    images = ProductImageSerializers(many=True)
    variants = VariantSerializers(many=True)

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        images = validated_data.pop('images')
        variants = validated_data.pop('variants')
        product = Product.objects.create(**validated_data)
        for image in images:
            ProductImage.objects.create(product=product, **image)
        for variant in variants:
            ProductVariantPrice.objects.create(product=product,**variant)
        return product
