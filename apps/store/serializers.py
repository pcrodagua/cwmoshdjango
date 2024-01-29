from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from apps.store.models import Product, Collection
from decimal import Decimal


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ["id", "title", "products_count"]

    products_count = serializers.IntegerField()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "description", "slug", "inventory", "unit_price", "price_with_tax", "collection"]

    price_with_tax = serializers.SerializerMethodField(
        method_name="calculate_tax")

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)

# this other way requires a view creation on view.py, the view should be named as view_name
# it also has to be specified in the urls
# class ProductSerializer(ModelSerializer):
#     price_with_tax = serializers.SerializerMethodField(method_name="calculate_tax")
#     collection = serializers.HyperlinkedRelatedField(
#         queryset=Collection.objects.all(),
#         view_name="collection-detail"
#     )
# 
#     def calculate_tax(self, product: Product):
#         return product.unit_price * Decimal(1.15)
# 
#     class Meta:
#         model = Product
#         fields = ["id", "title", "description", "slug", "inventory", "unit_price", "price_with_tax", "collection"]

# Returns the class collection serialized in the collection
# class ProductSerializer(ModelSerializer):
#     price_with_tax = serializers.SerializerMethodField(method_name="calculate_tax")
#     collection = CollectionSerializer()
#
#     def calculate_tax(self, product: Product):
#         return product.unit_price * Decimal(1.15)
#
#     class Meta:
#         model = Product
#         fields = (
#             "id",
#             "title",
#             "unit_price",
#             "price_with_tax",
#             "collection",
#         )

# just returns the string representation, but this should be changed on the views
# setting a Model.objects.select_related to preload the data from the FK
# class ProductSerializer(ModelSerializer):
#     price_with_tax = serializers.SerializerMethodField(method_name="calculate_tax")
#     collection = serializers.StringRelatedField()
#
#     def calculate_tax(self, product: Product):
#         return product.unit_price * Decimal(1.15)
#
#     class Meta:
#         model = Product
#         fields = (
#             "id",
#             "title",
#             "slug",
#             "description",
#             "unit_price",
#             "price_with_tax",
#             "collection",
#         )
