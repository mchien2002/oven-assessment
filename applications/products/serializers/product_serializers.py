from rest_framework import serializers

from applications.products.models.product import Product


class ProductCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    price = serializers.FloatField(min_value=1000)
    is_active = serializers.BooleanField(default=True)


class ProductUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, required=False)
    description = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    price = serializers.FloatField(min_value=1000, required=False)
    is_active = serializers.BooleanField(default=True, required=False)


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "description",
            "price",
            "image_url",
            "is_active",
            "created_at",
            "updated_at",
        )


class ProductResponseSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "image_url",
            "created_at",
            "updated_at",
        )

    @staticmethod
    def get_image_url(obj):
        return obj.get("image_url")
