"""Django admin modification - tests"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


class AdminPageTests(TestCase):
    def setUp(self):
        """user and client CREATE"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='streleadmintest@example.com',
            password='testitest'
        )

        # used force_login to make sure this admin user is logged in for other tests
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='createthisuser@example.com',
            password='testitest'
        )

    def test_users_list(self):
        """Test if users are listed on site"""

        # use Django-URL reversing system to get page that shows list of users
        url = reverse('admin:users_user_changelist')
        response = self.client.get(url)

        self.assertContains(response, self.user)

    def test_edit_user(self):
        """Test if the edit user page works, when clicked on user"""
        url = reverse('admin:users_user_change', args=[self.user.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_create_user(self):
        """Test if creating a new user works"""
        url = reverse('admin:users_user_add')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
