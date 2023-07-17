from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import authentication
from rest_framework import status
from rest_framework.response import Response
from django.contrib.gis.geos import Point

from suppliersarea.models import ServiceArea
from suppliersarea.serializers import ServiceAreaSerializer


class FindAreaView(APIView):
    """
    This
    """
    authentication_classes = [authentication.TokenAuthentication]

    def post(self, request, pk=None, format=None) -> Response:
        """
        This is the main endpoint for this service. It provides returns a lit of providers for a specific location given by the user.
        This functions runs a query for service areas that matches the location given location and returns list of providers and the price to server that location.

        **Parameters:**
        lat - the latitude
        lng - the longitude
        """

        """ For listing out a single post, HTTP method: GET """
        latitude = float(request.data['lat'])
        longitude = float(request.data['lng'])
        pnt = Point(longitude, latitude)

        areas = ServiceArea.objects.filter(information__contains=pnt)

        serializer = ServiceAreaSerializer(areas, many=True)
        return Response(serializer.data,
                        status=status.HTTP_200_OK)
