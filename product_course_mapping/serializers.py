from rest_framework import serializers
from .models import ProductCourseMapping


class ProductCourseMappingSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCourseMapping
        fields = "__all__"

    def validate(self, data):

        product = data.get("product")
        primary = data.get("primary_mapping")

        if primary:

            exists = ProductCourseMapping.objects.filter(
                product=product,
                primary_mapping=True
            ).exists()

            if exists:
                raise serializers.ValidationError(
                    "Product already has primary course."
                )

        return data