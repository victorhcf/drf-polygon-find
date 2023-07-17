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
        """
        This a the view for the custom page and it is created only to allow easy testing of the 
        main endpoint of this project directly on the admin using this custom view

        This endpoint receits an location (latitude, longitude) and returns the providers that can serve on the location based on the service area.
        **Template:**

        :template:`templates/admin/custom_page.html`

        **Parameters:**
        latitude - the latitude
        longitude - the longitude
        """
        latitude = float(request.data['latitude'])
        longitude = float(request.data['longitude'])

        host = str(get_current_site(request))
        url = 'http://' + host + '/findarea/'
        myobj = {'lat': latitude, 'lng': longitude}
        response = requests.post(url, json=myobj)

        areas_json = response.json()
        areas = []
        for area in areas_json:
            areas.append(ServiceArea.objects.get(id=area.get('id')))

        return render(request, 'admin/custom_page.html', locals())
