
from rest_framework.views import APIView
from rest_framework import authentication
from rest_framework import status
from rest_framework.response import Response
from django.contrib.gis.geos import Point

from suppliersarea.models import ServiceArea
from suppliersarea.serializers import ServiceAreaSerializer


class FindAreaView(APIView):
    """
    View class for querying areas by specific location (latitude and longitude). endpoint: /findarea/
    """
    authentication_classes = [authentication.TokenAuthentication]

    def post(self, request, pk=None, format=None) -> Response:
        """ For listing out a single post, HTTP method: GET """
        latitude = float(request.data['lat'])
        longitude = float(request.data['lng'])
        pnt = Point(longitude, latitude)

        areas = ServiceArea.objects.filter(information__contains=pnt)

        serializer = ServiceAreaSerializer(areas, many=True)
        return Response(serializer.data,
                        status=status.HTTP_200_OK)
