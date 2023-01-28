from django.test import TestCase
from rest_framework.test import APIClient


class ViewsTest(TestCase):

    def test_should_see_200_after_get_all_tasks(self):
        """GET all todos via /todos/ endpoint"""
        client = APIClient()
        res = client.get('/todos/')

        self.assertEqual(res.status_code, 200)
