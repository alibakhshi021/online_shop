from django.test import TestCase, Client
from django.urls import reverse
from ..models import Product, ProductBrand, ProductCategory

class TestProductListView(TestCase):

    def setUp(self):
        self.category = ProductCategory.objects.create(title='test category', url_title='test-cat',is_active=True,
            is_delete=False)
        self.brand = ProductBrand.objects.create(title='test brand', url_title='test-brand', is_active=True)

        self.product1 = Product.objects.create(
            title='iphone 15 pro',
            brand=self.brand,
            stock_quantity=2,
            price=100,
            short_description='alert2025',
            description='2025American',
            is_active=True,
            is_delete=False
        )

        self.product2 = Product.objects.create(
            title='iphone 16 pro',
            brand=self.brand,
            stock_quantity=2,
            price=500,
            short_description='alert2025',
            description='2025American',
            is_active=True,
            is_delete=False
        )

        self.product3 = Product.objects.create(
            title='iphone 17 pro',
            brand=self.brand,
            stock_quantity=2,
            price=900,
            short_description='alert',
            description='2025American',
            is_active=True,
            is_delete=False
        )

        self.url = reverse('product:product-list')  # یا '/products/' اگه reverse کار نکنه
        self.product1.category.set([self.category])
        self.product2.category.set([self.category])
        self.product3.category.set([self.category])
        
    def test_view_statues_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_start_price_filtering(self):   
        response = self.client.get(self.url + '?start_price=600')
        self.assertEqual(len(response.context['products']), 1)
        self.assertEqual(response.context['products'][0].title, 'iphone 17 pro')

    def test_end_price_filtering(self):   
        response = self.client.get(self.url + '?end_price=200')
        self.assertEqual(len(response.context['products']), 1)
        self.assertEqual(response.context['products'][0].title, 'iphone 15 pro')    


    def test_brand_filtering(self):
        url = reverse('product:product-brand-list', kwargs={'brand': 'test-brand'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['products']), 3)

    def test_category_filtering(self):
        url = reverse('product:product-category-list', kwargs={'cat': 'test-cat'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.content['products']), 3)    