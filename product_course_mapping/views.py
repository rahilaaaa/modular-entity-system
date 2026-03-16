from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import ProductCourseMapping
from .serializers import ProductCourseMappingSerializer


class ProductCourseMappingListCreateAPIView(APIView):

    def get(self, request):

        product_id = request.query_params.get("product_id")

        queryset = ProductCourseMapping.objects.filter(is_active=True)

        if product_id:
            queryset = queryset.filter(product_id=product_id)

        serializer = ProductCourseMappingSerializer(queryset, many=True)

        return Response(serializer.data)


    def post(self, request):

        serializer = ProductCourseMappingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)



class ProductCourseMappingDetailAPIView(APIView):

    def get_object(self, pk):

        try:
            return ProductCourseMapping.objects.get(pk=pk)

        except ProductCourseMapping.DoesNotExist:
            return None


    def get(self, request, pk):

        obj = self.get_object(pk)

        if not obj:
            return Response({"error": "Mapping not found"}, status=404)

        serializer = ProductCourseMappingSerializer(obj)

        return Response(serializer.data)


    def delete(self, request, pk):

        obj = self.get_object(pk)

        if not obj:
            return Response({"error": "Mapping not found"}, status=404)

        obj.delete()

        return Response(status=204)