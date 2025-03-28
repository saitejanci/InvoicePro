from django.test import TestCase
from django.urls import reverse

class TestCase(TestCase):
    def test_home_view(self):
        """Test if login page returns 200 status"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
