from django.test import TestCase
from django.urls import reverse

class TestCase(TestCase):
    def test_home_view(self):
        """Test if login page returns 200 status"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    def test_view_invoice_page_loads(self):
        """Test if view_invoice page returns 200 status"""
        response = self.client.get(reverse('view_invoice'))
        self.assertEqual(response.status_code, 200)
    def test_view_invoice_uses_correct_template(self):
        """Test if correct template is used for invoice page"""
        response = self.client.get(reverse('view_invoice'))
        self.assertTemplateUsed(response, 'invoice/view_invoice.html')
