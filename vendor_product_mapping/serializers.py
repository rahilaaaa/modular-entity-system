from rest_framework import serializers
from .models import VendorProductMapping

class VendorProductMappingSerializer(serializers.ModelSerializer):

    class Meta:
        model = VendorProductMapping
        fields = "__all__"

    def validate(self, data):

        vendor = data.get("vendor")
        primary = data.get("primary_mapping")

        if primary:

            exists = VendorProductMapping.objects.filter(
                vendor=vendor,
                primary_mapping=True
            ).exists()

            if exists:
                raise serializers.ValidationError(
                    "Vendor already has primary product."
                )

        return data