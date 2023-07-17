from django.test import TestCase
from django.contrib.gis.geos import Polygon
from suppliersarea.models import Provider, ServiceArea


class ProviderModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Provider.objects.create(name='testum',
                                email='testum@email.com', phonenumber='3311',
                                language='eng', currency='USD')

    def test_name_label(self):
        provider = Provider.objects.get(id=1)
        field_label = provider._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name(self):
        provider = Provider.objects.get(id=1)
        self.assertEqual(provider.name, 'testum')

    def test_string(self):
        provider = Provider.objects.get(id=1)
        self.assertEqual(str(provider), 'testum')


class ServiceAreaModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        provider2 = Provider.objects.create(name='provider two',
                                            email='providertwo@email.com', phonenumber='2211',
                                            language='por', currency='BRL')

        poly_natal = Polygon(((-35.37777481283594, -5.719169558067793), (-35.3998765128905, -5.966521746780532), (-35.014201846938185, -
                             5.969819032478712), (-35.01972727195182, -5.719169558067793), (-35.37777481283594, -5.719169558067793)))

        poly_newyork = Polygon(((-74.83588358985594, 41.23082234798603), (-74.85550595612166, 40.41414448392849), (-72.3111391303344,
                               40.38425776292436), (-72.29151676406867, 41.19145795634718), (-74.83588358985594, 41.23082234798603)))

        ServiceArea.objects.create(name='area natal',
                                   price='1', provider=provider2, information=poly_natal)

        ServiceArea.objects.create(name='area newyork',
                                   price='10', provider=provider2, information=poly_newyork)

    def test_name_label(self):
        area = ServiceArea.objects.get(id=1)
        field_label = area._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name(self):
        area = ServiceArea.objects.get(id=1)
        self.assertEqual(area.name, 'area natal')
