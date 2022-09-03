from django.test import TestCase
from django.urls import resolve
from checks.views import home

### Unit tests
class TestViews(TestCase):
    def test_if_root_url_resolves_to_home(self):
        '''
         Check if Django is getting the correct
         view it expects when calling the site's root
        '''
        found = resolve('/')
        self.assertEqual(found.func, home)


    def test_if_home_template_renders(self):
        '''
         Check if the home view renders OK
        '''
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)