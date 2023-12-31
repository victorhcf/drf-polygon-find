from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from suppliersarea.models import Provider
from suppliersarea.serializers import ProviderSerializer


class ProviderListView(APIView):
    """
    API endpoint that allows providers to be viewed or edited.
    """
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None) -> Response:
        """ For listing out the providers, HTTP method: GET """
        providers = Provider.objects.all()
        # Passing the queryset through the serializer
        serializer = ProviderSerializer(providers, many=True)
        return Response(serializer.data,
                        status=status.HTTP_200_OK)

    def post(self, request, format=None) -> Response:
        """ For creating a new Provider, HTTP method: POST """
        serializer = ProviderSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


class ProviderDetailView(APIView):
    """
    View class for listing, updating and deleting a single Provider, endpoint: /providers/<int:pk>/
    """
    authentication_classes = [authentication.TokenAuthentication]

    def get(self, request, pk=None, format=None) -> Response:
        """ For listing out a single providers, HTTP method: GET """
        provider = get_object_or_404(Provider.objects.all(), pk=pk)
        serializer = ProviderSerializer(provider)
        return Response(serializer.data,
                        status=status.HTTP_200_OK)

    def put(self, request, pk=None, format=None):
        """ For updating an existing Provider, HTTP method: PUT """
        provider = get_object_or_404(Provider.objects.all(), pk=pk)
        serializer = ProviderSerializer(provider, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, format=None) -> Response:
        """ For deleting a Provider, HTTP method: DELETE """
        provider = get_object_or_404(Provider.objects.all(), pk=pk)
        provider.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
