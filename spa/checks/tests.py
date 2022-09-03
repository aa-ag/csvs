from django.test import TestCase
from django.urls import resolve
from checks.views import home

### Unit tests
class TestViews(TestCase):
    def test_if_root_url_resolves_to_home(self):
        '''
        '''
        found = resolve('/')
        self.assertEqual(found.func, home)


    def test_if_home_template_renders(self):
        '''
        '''
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)