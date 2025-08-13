from django.urls import resolve, reverse
from django.test import SimpleTestCase
from ..views import ContactUsView, CreateProfileView, ProfilesView


class TestContactView(SimpleTestCase):

    def test_contact_module_url_resolve(self):
        url = reverse("contact_module")
        self.assertEqual(resolve(url).func.view_class, ContactUsView)

    def tets_create_module_url_resolve(self):
        url = reverse("create_profile_page")
        self.assertEqual(resolve(url).func.view_class, CreateProfileView)

    def test_profile_module_url_resolve(self):
        url = reverse("profiles_page")
        self.assertEqual(resolve(url).func.view_class, ProfilesView)
