from django.test import TestCase

### Unit tests
### --- VIEWS -----------------------------------------------------------------
class TestViews(TestCase):
    def test_if_home_template_renders(self):
        '''
         python manage.py test checks.tests.TestViews.is_home_html_rendered
        '''
        response = self.client.get('')
        print("\nStatus code:", response.status_code)
        self.assertEqual(response.status_code, 200)


    def test_if_report_template_renders(self):
        '''
         python manage.py test checks.tests.TestViews.is_home_html_rendered
        '''
        response = self.client.get('report')
        print("\nStatus code:", response.status_code)
        self.assertEqual(response.status_code, 200)