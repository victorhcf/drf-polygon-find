from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import authentication
from rest_framework.response import Response
from django.contrib.sites.shortcuts import get_current_site
import requests

from suppliersarea.models import ServiceArea

class FindProviderView(APIView):
    """
    View class for querying areas by specific location (latitude and longitude). endpoint: /findarea/
    """
    authentication_classes = [authentication.TokenAuthentication]

    def post(self, request, format=None) -> Response:
        """ For listing out a single post, HTTP method: GET """
        latitude = float(request.data['latitude'])
        longitude = float(request.data['longitude'])
        
        host = str(get_current_site(request))
        url = 'http://' + host + '/findarea/'
        myobj = {'lat': latitude, 'lng': longitude}
        response = requests.post(url, json = myobj)

        areas_json = response.json()
        areas = []
        for area in areas_json:
            areas.append( ServiceArea.objects.get(id=area.get('id')) )

        return render(request, 'admin/custom_page.html', locals())