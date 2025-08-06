from django.test import TestCase
from ..models import ContactUs


class TestContactModel(TestCase):
    def test_contact_us_with_valid_data(self):
        contactus = ContactUs.objects.create(
            full_name= "test user",
            email= "test@example.com",
            title= "test title",
            message= "this is a test message"
        )
        self.assertEqual(contactus.email, "test@example.com")