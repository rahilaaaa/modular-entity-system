from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Certification
from .serializers import CertificationSerializer


class CertificationListCreateAPIView(APIView):

    def get(self, request):

        certifications = Certification.objects.filter(is_active=True)
        serializer = CertificationSerializer(certifications, many=True)

        return Response(serializer.data)


    def post(self, request):

        serializer = CertificationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)



class CertificationDetailAPIView(APIView):

    def get_object(self, pk):

        try:
            return Certification.objects.get(pk=pk)

        except Certification.DoesNotExist:
            return None


    def get(self, request, pk):

        obj = self.get_object(pk)

        if not obj:
            return Response({"error": "Certification not found"}, status=404)

        serializer = CertificationSerializer(obj)

        return Response(serializer.data)


    def put(self, request, pk):

        obj = self.get_object(pk)

        serializer = CertificationSerializer(obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)


    def patch(self, request, pk):

        obj = self.get_object(pk)

        serializer = CertificationSerializer(obj, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)


    def delete(self, request, pk):

        obj = self.get_object(pk)

        if not obj:
            return Response({"error": "Certification not found"}, status=404)

        obj.delete()

        return Response(status=204)