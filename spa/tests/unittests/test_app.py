### external
from django.test import TestCase
import os
from dotenv import load_dotenv
### relative
import spa.settings as settings

load_dotenv()

### Unit tests
class TestViews(TestCase):
    def test_that_checks_is_in_app(self):
        self.assertTrue("checks" in settings.INSTALLED_APPS)

    def test_apps_language(self):
        self.assertEqual('en-us', settings.LANGUAGE_CODE)

    def test_apps_time_zone(self):
        self.assertEqual('UTC', settings.TIME_ZONE)

    def test_allowed_hosts(self):
        self.assertIn("*", settings.ALLOWED_HOSTS)

    def test_that_debug_is_false(self):
        self.assertTrue(settings.DEBUG==False)

    def test_that_key_is_not_none(self):
        sk = os.environ.get("SECRET_KEY")
        self.assertIsNotNone(sk)
