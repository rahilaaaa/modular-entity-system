from rest_framework import serializers
from .models import CourseCertificationMapping


class CourseCertificationMappingSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseCertificationMapping
        fields = "__all__"

    def validate(self, data):

        course = data.get("course")
        primary = data.get("primary_mapping")

        if primary:

            exists = CourseCertificationMapping.objects.filter(
                course=course,
                primary_mapping=True
            ).exists()

            if exists:
                raise serializers.ValidationError(
                    "Course already has primary certification."
                )

        return data