from django.test import TestCase, Client

class TestViews(TestCase):
    def is_home_html_rendered(self):
        '''
         python manage.py test checks.tests.TestViews.is_home_html_rendered
        '''
        client = Client()
        response = self.client.get('')
        print("\nStatus code:", response.status_code)
        self.assertEqual(response.status_code, 200)