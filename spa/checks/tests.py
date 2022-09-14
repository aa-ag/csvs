### external
from urllib import response
from django.test import TestCase
from django.http import HttpRequest
### relative
from django.urls import resolve
from checks.views import home

### Unit tests
class TestViews(TestCase):
    def test_if_root_url_resolves_to_home(self):
        '''
         Check if Django is getting the correct
         view it expects when calling the site's root
        '''
        found = resolve("/")
        self.assertEqual(found.func, home)


    def test_if_home_template_renders(self):
        '''
         Check if the home view renders OK
        '''
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)


    def test_if_home_template_returns_correct_html(self):
        '''
         Check that the home() view is rendering the
         expected template
        '''
        request = HttpRequest()
        response = home(request)
        html = response.content.decode("utf-8")
        self.assertIn("<title> checks </title>", html)

    
    def test_if_home_contains_csrf_token(self):
        response = self.client.get("")
        self.assertIn("csrf_token", response.context)

    def test_home_form(self):
        with open("static/samples/constructors_sample.csv") as f:
            response = self.client.post("/report", {"file":f})
            self.assertEqual(response.status_code, 200)
    
    def test_home_form_passes_with_correct_file(self):
        with open("static/samples/utf8_users.csv") as f:
            notok = "has </b>passed</b> the minimun requirenments."
            response = self.client.post("/report", {"file":f})
            html = response.content.decode("utf-8")
            self.assertIn(notok, html)

    def test_home_form_fails_with_wrong_file(self):
        with open("static/samples/constructors_sample.csv") as f:
            notok = "<b>needs review</b>: some requirenments are not yet met."
            response = self.client.post("/report", {"file":f})
            html = response.content.decode("utf-8")
            self.assertIn(notok, html)
    
    # def test_home_form_response_includes_all_parameters(self):
    #     with open("static/samples/constructors_sample.csv") as f:
    #         response = self.client.post("/report", {"file":f})

    #         for element in response.context:
    #             for j in element:
    #                 print(j)
    #                 self.assertIn("isutf8_encoded", j)