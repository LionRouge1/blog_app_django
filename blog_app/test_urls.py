from django.test import TestCase
from django.urls import reverse

class HttpResponseTests(TestCase):
  def test_home_page_status(self):
    "Url return 200 for the request status code and contain home page"
    response = self.client.get(reverse('home'))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, 'home page')

  def test_about_page_status(self):
    "Return 200 for the request status and contain the about page"
    response = self.client.get(reverse('about'))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, 'about page')