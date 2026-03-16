from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import CourseCertificationMapping
from .serializers import CourseCertificationMappingSerializer


class CourseCertificationMappingListCreateAPIView(APIView):

    def get(self, request):

        course_id = request.query_params.get("course_id")

        queryset = CourseCertificationMapping.objects.filter(is_active=True)

        if course_id:
            queryset = queryset.filter(course_id=course_id)

        serializer = CourseCertificationMappingSerializer(queryset, many=True)

        return Response(serializer.data)


    def post(self, request):

        serializer = CourseCertificationMappingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)



class CourseCertificationMappingDetailAPIView(APIView):

    def get_object(self, pk):

        try:
            return CourseCertificationMapping.objects.get(pk=pk)

        except CourseCertificationMapping.DoesNotExist:
            return None


    def get(self, request, pk):

        obj = self.get_object(pk)

        if not obj:
            return Response({"error": "Mapping not found"}, status=404)

        serializer = CourseCertificationMappingSerializer(obj)

        return Response(serializer.data)


    def delete(self, request, pk):

        obj = self.get_object(pk)

        if not obj:
            return Response({"error": "Mapping not found"}, status=404)

        obj.delete()

        return Response(status=204)