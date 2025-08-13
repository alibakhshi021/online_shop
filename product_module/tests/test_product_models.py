from django.test import TestCase
from ..models import (
    Product,
    ProductCategory,
    ProductBrand,
    ProductTag,
    ProductGallery,
    ProductVisit,
)


class TestProductCategoryModel(TestCase):

    def test_product_category_with_valid_data(self):
        category = ProductCategory.objects.create(
            title="test",
            url_title="test",
            is_active=True,
            is_delete=False,
        )
        self.assertEqual(category.title, "test")


class TestProductBrandModel(TestCase):

    def test_product_brand_with_valid_data(self):
        brand = ProductBrand.objects.create(title="LG", url_title="LG", is_active=True)
        self.assertEqual(brand.title, "LG")


class TestProductModel(TestCase):

    def setUp(self):
        self.cat1 = ProductCategory.objects.create(
            title="test",
            url_title="test",
            is_active=True,
            is_delete=False,
        )

        self.brand = ProductBrand.objects.create(
            title="LG", url_title="LG", is_active=True
        )

    def test_create_product_with_relations(self):

        product = Product.objects.create(
            title="iphone 15 pro",
            brand=self.brand,
            stock_quantity=2,
            price=15000000,
            short_description="2025",
            description="2025American",
            is_active=True,
            is_delete=False,
        )

        product.category.set([self.cat1])
        product.save()

        self.assertEqual(product.title, "iphone 15 pro")
        self.assertEqual(product.get_in_is_active(), "موجود میباشد")
        self.assertIn(self.cat1, product.category.all())


class TestProductTagModel(TestCase):

    def setUp(self):
        self.category = ProductCategory.objects.create(
            title="test",
            url_title="test",
            is_active=True,
            is_delete=False,
        )

        self.brand = ProductBrand.objects.create(
            title="LG", url_title="LG", is_active=True
        )

        self.product = Product.objects.create(
            title="iphone 15 pro",
            brand=self.brand,
            stock_quantity=2,
            price=15000000,
            short_description="2025",
            description="2025American",
            is_active=True,
            is_delete=False,
        )

        self.product.category.set([self.category])

    def test_product_tag(self):
        tag = ProductTag.objects.create(product=self.product, caption="2025")
        self.assertEqual(tag.product, self.product)
