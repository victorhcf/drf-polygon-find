from rest_framework.test import APITestCase
from suppliersarea.login import login
from suppliersarea.models import Provider


class BasicTest(APITestCase):
    @classmethod
    def setUpTestData(self):
        # Set up non-modified objects used by all test methods

        self.client_object, self.user = login(self, 'dummy')
        self.content_type = 'application/json'

        Provider.objects.create(name='john galt',
                                email='johngalt@email.com', phonenumber='4411',
                                language='eng', currency='USD')

    def test_create_provider(self):
        data = {
            "name": "jon doe",
            "email": "jon@doe.com",
            "phonenumber": "087",
            "language": "por",
            "currency": "BRL",
        }
        response = self.client_object.post('/providers/', data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data.get('name'), 'jon doe')

    def test_retrieveall_provider(self):
        response = self.client_object.get('/providers/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0].get('name'), 'john galt')

    def test_retrieveone_provider(self):
        response = self.client_object.get('/providers/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get('name'), 'john galt')

    def test_update_provider(self):
        response_retrieving = self.client_object.get('/providers/1/')
        dict_galt = response_retrieving.data
        dict_galt['name'] = 'who is john galt?'

        response = self.client_object.put(
            '/providers/1/', dict_galt, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get('name'), 'who is john galt?')

        response_retrieving = self.client_object.get('/providers/1/')
        self.assertEqual(response_retrieving.status_code, 200)
        self.assertEqual(response_retrieving.data.get(
            'name'), 'who is john galt?')

    def test_delete_provider(self):
        response = self.client_object.delete('/providers/1/')
        self.assertEqual(response.status_code, 204)

        response_retrieving2 = self.client_object.get('/providers/1/')
        self.assertEqual(response_retrieving2.status_code, 404)
