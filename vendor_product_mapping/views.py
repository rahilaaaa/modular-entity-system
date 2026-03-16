from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import VendorProductMapping
from .serializers import VendorProductMappingSerializer


class VendorProductMappingListCreateAPIView(APIView):

    def get(self, request):

        vendor_id = request.query_params.get("vendor_id")

        queryset = VendorProductMapping.objects.filter(is_active=True)

        if vendor_id:
            queryset = queryset.filter(vendor_id=vendor_id)

        serializer = VendorProductMappingSerializer(queryset, many=True)

        return Response(serializer.data)


    def post(self, request):

        serializer = VendorProductMappingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)



class VendorProductMappingDetailAPIView(APIView):

    def get_object(self, pk):

        try:
            return VendorProductMapping.objects.get(pk=pk)

        except VendorProductMapping.DoesNotExist:
            return None


    def get(self, request, pk):

        obj = self.get_object(pk)

        if not obj:
            return Response({"error": "Mapping not found"}, status=404)

        serializer = VendorProductMappingSerializer(obj)

        return Response(serializer.data)


    def put(self, request, pk):

        obj = self.get_object(pk)

        serializer = VendorProductMappingSerializer(obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)


    def patch(self, request, pk):

        obj = self.get_object(pk)

        serializer = VendorProductMappingSerializer(obj, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)


    def delete(self, request, pk):

        obj = self.get_object(pk)

        if not obj:
            return Response({"error": "Mapping not found"}, status=404)

        obj.delete()

        return Response(status=204)