from rest_framework.test import APITestCase
from django.contrib.gis.geos import Polygon

from suppliersarea.login import login
from suppliersarea.models import Provider, ServiceArea


class BasicTest(APITestCase):
    @classmethod
    def setUpTestData(self):
        # Set up non-modified objects used by all test methods

        self.client_object, self.user = login(self, 'dummy')
        self.content_type = 'application/json'

        galt = Provider.objects.create(name='john galt',
                                       email='johngalt@email.com', phonenumber='4411',
                                       language='eng', currency='USD')

        poly_newyork = Polygon(((-74.83588358985594, 41.23082234798603), (-74.85550595612166, 40.41414448392849), (-72.3111391303344,
                               40.38425776292436), (-72.29151676406867, 41.19145795634718), (-74.83588358985594, 41.23082234798603)))
        poly_wonderland = Polygon(((-35.37777481283594, -5.719169558067793), (-35.3998765128905, -5.966521746780532),
                                  (-35.014201846938185, -5.969819032478712), (-35.01972727195182, -5.719169558067793), (-35.37777481283594, -5.719169558067793)))

        ServiceArea.objects.create(name='area newyork',
                                   price='10', provider=galt, information=poly_newyork)

        ServiceArea.objects.create(name='area wonderland',
                                   price='1', provider=galt, information=poly_wonderland)

    def test_create_servicearea(self):
        poly_losangeles = """{
            "type": "Polygon",
            "coordinates": [
                [
                    [-119.34613347632094, 34.34344955490531],
                    [-116.76244261768204, 34.26985599433595],
                    [-116.73004524014424, 33.08363729997903],
                    [-119.41092823139653, 33.11756192953386],
                    [-119.34613347632094, 34.34344955490531]
                ]
            ]
        }"""

        joe = Provider.objects.create(name='joe biden',
                                      email='joebiden@email.com', phonenumber='6688',
                                      language='por', currency='BRL')
        data = {
            "name": "los angeles",
            "price": 20,
            "provider": joe.id,
            "information": poly_losangeles,
        }
        response = self.client_object.post('/serviceareas/', data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data.get('name'), 'los angeles')

    def test_retrieveall_servicearea(self):
        response = self.client_object.get('/serviceareas/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0].get('name'), 'area newyork')
        self.assertEqual(len(response.data), 2)

    def test_retrieveone_v(self):
        response = self.client_object.get('/serviceareas/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get('name'), 'area newyork')

    def test_update_servicearea(self):
        response_retrieving = self.client_object.get('/serviceareas/1/')
        dict_newyork = response_retrieving.data
        dict_newyork['name'] = 'area hawaii'

        response = self.client_object.put(
            '/serviceareas/1/', dict_newyork, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get('name'), 'area hawaii')

        response_retrieving = self.client_object.get('/serviceareas/1/')
        self.assertEqual(response_retrieving.status_code, 200)
        self.assertEqual(response_retrieving.data.get('name'), 'area hawaii')

    def test_delete_servicearea(self):
        response = self.client_object.delete('/serviceareas/1/')
        self.assertEqual(response.status_code, 204)

        response_retrieving2 = self.client_object.get('/serviceareas/1/')
        self.assertEqual(response_retrieving2.status_code, 404)
