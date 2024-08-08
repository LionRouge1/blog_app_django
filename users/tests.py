from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class HttpRequestTest(TestCase):
  def test_user_index_page_status(self):
    response = self.client.get(reverse('user:index'))