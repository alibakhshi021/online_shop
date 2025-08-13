# import pytest
# from rest_framework.test import APIClient
# from django.urls import reverse
# from account_module.models import User
# @pytest.fixture
# def api_client():
#     client = APIClient()
#     return client

# @pytest.fixture
# def common_user():
#     user = User.objects.create_user(username="mohamad", password="Nima4030#", is_verified=True)
#     return user


# # دسترسی کلاس رو بهش میدیم
# @pytest.mark.django_db


# class TestProductApi:
#     client = APIClient()

#     def test_get_product_response_200_status(self, api_client):
#         url = reverse('api-v1:post-list')
#         response = api_client.get(url)
#         assert response.status_code == 200

#     def test_create_product_response_401_status(self, api_client):
#         url =  reverse('api-v1:post-list')
#         data = {

#             'title' : 'iphone 15 pro',
#             'stock_quantity' : 2,
#             'price' : 15000000,
#             'short_description' : '2025',
#             'description' : '2025American',
#             'is_active' : True,
#             'is_delete' : False,
#         }
#         # api_client.force_authenticate(user={})
#         response = api_client.post(url, data)
#         assert response.status_code == 401

#     def test_create_product_response_201_status(self, api_client, common_user):
#         url =  reverse('api-v1:post-list')
#         data = {

#             'title' : 'iphone 15 pro',
#             'stock_quantity' : 2,
#             'price' : 15000000,
#             'short_description' : '2025',
#             'description' : '2025American',
#             'is_active' : True,
#             'is_delete' : False,
#         }

#         user = common_user
#         api_client.force_authenticate(user=user)
#         response = api_client.post(url, data)
#         assert response.status_code == 201


import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from account_module.models import User
from product_module.models import ProductCategory, Product


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def common_user():
    user = User.objects.create_user(
        username="mohamad", password="Nima4030#", is_verified=True
    )
    return user


@pytest.mark.django_db
class TestProductApi:

    def test_get_product_response_200_status(self, api_client):
        url = reverse("api-v1:post-list")
        response = api_client.get(url)
        assert response.status_code == 200

    def test_create_product_response_401_status(self, api_client):
        url = reverse("api-v1:post-list")
        data = {
            "title": "iphone 15 pro",
            "stock_quantity": 2,
            "price": 15000000,
            "short_description": "2025",
            "description": "2025American",
            "is_active": True,
            "is_delete": False,
        }
        # کاربر لاگین نکرده
        response = api_client.post(url, data, format="json")
        assert response.status_code == 401

    def test_create_product_response_201_status(self, api_client, common_user):
        url = reverse("api-v1:post-list")

        # ایجاد یک category معتبر
        category = ProductCategory.objects.create(
            title="test-cat", is_active=True, is_delete=False
        )

        data = {
            "title": "iphone 15 pro",
            "stock_quantity": 2,
            "category": category.id,
            "price": 15000000,
            "short_description": "2025",
            "description": "2025American",
            "is_active": True,
            "is_delete": False,
        }

        api_client.force_authenticate(user=common_user)
        response = api_client.post(url, data, format="json")
        assert response.status_code == 201

        # بررسی اینکه محصول واقعاً ساخته شده
        assert Product.objects.filter(title="iphone 15 pro", category=category).exists()
