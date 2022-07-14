from django.contrib import admin

# Register your models here.
from .models import Product,ProductImage,ProductVariant,ProductVariantPrice,Variant
admin.site.register([Product,ProductImage,ProductVariant,Variant])


"""
Product table 
Product Variant table 
Product Image
"""