### external
from django.test import TestCase
### relative
import spa.settings as settings

### Unit tests
class TestViews(TestCase):
    def test_that_checks_is_in_app(self):
        self.assertTrue("checks" in settings.INSTALLED_APPS)

    def test_that_debug_is_false(self):
        self.assertTrue(settings.DEBUG==False)
