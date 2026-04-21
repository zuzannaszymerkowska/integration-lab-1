from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse

class BlogTests(TestCase):
    def test_homepage_status_code(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 400)

    def test_api_status_code(self):
        response = self.client.get(reverse('api_posts_json'))
        self.assertEqual(response.status_code, 400)