from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import authentication
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from suppliersarea.serializers import ServiceAreaSerializer
from .models import ServiceArea

class ServiceAreaListView(APIView):
    """
    API endpoint that allows ServiceArea to be viewed or edited.
    """
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer

    def get(self, request, format=None) -> Response:
        """ For listing out the posts, HTTP method: GET """
        serviceAreas = ServiceArea.objects.all()
        # Passing the queryset through the serializer
        serializer = ServiceAreaSerializer(serviceAreas, many=True)
        return Response(serializer.data,
                        status=status.HTTP_200_OK)

    def post(self, request, format=None) -> Response:
        """ For creating a new post, HTTP method: POST """
        serializer = ServiceAreaSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


class ServiceAreaDetailView(APIView):
    """
    View class for listing, updating and deleting a single ServiceArea, endpoint: /servicearea/<int:pk>/
    """
    authentication_classes = [authentication.TokenAuthentication]

    def get(self, request, pk=None, format=None) -> Response:
        """ For listing out a single post, HTTP method: GET """
        serviceArea = get_object_or_404(ServiceArea.objects.all(), pk=pk)
        serializer = ServiceAreaSerializer(serviceArea)
        return Response(serializer.data,
                        status=status.HTTP_200_OK)

    def put(self, request, pk=None, format=None):
        """ For updating an existing post, HTTP method: PUT """
        serviceArea = get_object_or_404(ServiceArea.objects.all(), pk=pk)
        serializer = ServiceAreaSerializer(serviceArea, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, format=None) -> Response:
        """ For deleting a ServiceArea, HTTP method: DELETE """
        print('delete')
        print(pk)
        serviceArea = get_object_or_404(ServiceArea.objects.all(), pk=pk)
        serviceArea.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
