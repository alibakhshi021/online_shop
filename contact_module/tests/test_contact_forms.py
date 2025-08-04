from django.test import TestCase
from contact_module.formes import ContactUsModelForm

class TestContactForm(TestCase):

    def test_contact_form_valid_data(self):
        form = ContactUsModelForm(data={
            "full_name": "test user",
            "email": "test@example.com",
            "title": "test title",
            "message": "this is a test message"
        })
        self.assertTrue(form.is_valid())