from rest_framework.test import APITestCase
from suppliersarea.login import login
from suppliersarea.models import Provider, ServiceArea
from django.contrib.gis.geos import Polygon


class BasicTest(APITestCase):
    @classmethod
    def setUpTestData(self):
        # Set up non-modified objects used by all test methods

        self.client_object, self.user = login(self, 'dummy')
        self.content_type = 'application/json'

        galt = Provider.objects.create(name='john galt', 
                                email='johngalt@email.com', phonenumber='4411', 
                                language='eng', currency='USD')
        
        poly_newyork = Polygon(((-74.83588358985594, 41.23082234798603), (-74.85550595612166, 40.41414448392849), (-72.3111391303344, 40.38425776292436), (-72.29151676406867, 41.19145795634718), (-74.83588358985594, 41.23082234798603)))
        poly_wonderland = Polygon(((-35.37777481283594, -5.719169558067793), (-35.3998765128905, -5.966521746780532), (-35.014201846938185, -5.969819032478712), (-35.01972727195182, -5.719169558067793), (-35.37777481283594, -5.719169558067793)))
        
        ServiceArea.objects.create(name='area newyork', 
                                price='10', provider=galt, information=poly_newyork)

        ServiceArea.objects.create(name='area wonderland', 
                                price='1', provider=galt, information=poly_wonderland)
        
        

    def test_find_point_in_wonderland(self):
        #wonderland_point = Point(-5.866185, -35.184486)
        wonderland_point = {
            'lat': -5.866185,
            'lng': -35.184486
        }
        response = self.client_object.post('/findarea/', data=wonderland_point)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0].get('name'), 'area wonderland')
    
    def test_find_point_in_newyork(self):
        #wonderland_point = Point(-5.866185, -35.184486)
        newyork_point = {
            'lat': 40.784946,
            'lng': -73.968109
        }
        response = self.client_object.post('/findarea/', data=newyork_point)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0].get('name'), 'area newyork')
        

