from django.test import TestCase
from django.urls import reverse, resolve
from ..views import HomeView, AboutView


class TestView(TestCase):
    def test_home_index_url_resolve(self):
        url = reverse("index_page")
        self.assertEqual(resolve(url).func.view_class, HomeView)

    def test_home_about_url_resolve(self):
        url = reverse("about_page")
        self.assertEqual(resolve(url).func.view_class, AboutView)
