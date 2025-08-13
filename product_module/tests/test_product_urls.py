from django.test import SimpleTestCase
from ..views import ProductListView, ProductDetailView, AddProductFavorite
from django.urls import reverse, resolve


class TestProductView(SimpleTestCase):

    def test_product_list_module_url_resolve(self):
        url = reverse("product:product-list")
        self.assertEqual(resolve(url).func.view_class, ProductListView)

    def test_product_category_url_resolve(self):
        url = reverse("product:product-category-list", kwargs={"cat": "mobile"})

        self.assertEqual(resolve(url).func.view_class, ProductListView)

    def test_product_brand_url_resolve(self):
        url = reverse("product:product-brand-list", kwargs={"brand": "samsung"})

        self.assertEqual(resolve(url).func.view_class, ProductListView)

    def test_product_detail_module_url_resolve(self):
        url = reverse("product:product-details", kwargs={"slug": "xiaomi-poco-x7-pro"})

        self.assertEqual(resolve(url).func.view_class, ProductDetailView)
