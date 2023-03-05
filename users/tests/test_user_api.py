from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

# CREATE_USER_URL = reverse('create-user')
TOKEN_URL = reverse('user-token')
MY_USER_URL = reverse('my-user')


def create_test_user(**params):
    """Creates new user and gives him rights"""
    my_user = get_user_model().objects.create_user(**params)
    my_user.has_perm('auth.change_user')
    my_user.has_perm('auth.add_user')
    my_user.has_perm('auth.view_user')
    my_user.has_perm('auth.delete_user')

    return my_user


# PUBLIC (unauthenticated)
class PublicUserApiTests(TestCase):
    def get_user_auth_token(self, userBody):

        response = self.client.post(TOKEN_URL, userBody)

        self.assertIn('token', response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        return response.data.token

    def setUp(self):
        self.client = APIClient()

    def test_user_email_exists_should_fail_401(self):
        body = {
            'email': 'strelewebtest@example.com',
            'password': 'testitest'
        }

        create_test_user(**body)

        response = self.client.post(MY_USER_URL, body)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_user_auth_token(self):
        user_details = {
            'email': 'peter@example.com',
            'password': 'testitest'
        }
        create_test_user(**user_details)

        body = {
            'email': user_details['email'],
            'password': user_details['password']
        }

        response = self.client.post(TOKEN_URL, body)

        self.assertIn('token', response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user_auth_token_blank_password(self):
        """Test should return an error, when pw is blank"""

        body = {
            'email': 'peter@example.com',
            'password': ''
        }
        response = self.client.post(TOKEN_URL, body)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn('token', response.data)

    def test_create_user_auth_token_bad_creds(self):
        """Test should return error when credentials are invalid"""
        user_details = {
            'email': 'peter@examplecom',
            'password': 'testitest'
        }

        create_test_user(**user_details)

        body = {
            'email': user_details['email'],
            'password': user_details['password']
        }

        response = self.client.post(TOKEN_URL, body)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn('token', response.data)

    def test_retrieve_user_unautorized(self):
        """Test that authentication is required for MYUSER endpoint"""

        response = self.client.get(MY_USER_URL)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateUserApiTests(TestCase):
    """Require Authentication Tests"""

    def setUp(self):
        self.user = create_test_user(
            email='streletest@example.com',
            password='testitest'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_retrieve_profile_success(self):
        """get profile for logged in user"""
        response = self.client.get(MY_USER_URL)

        expectedResponse = {
            'id': 9, 'email': 'streletest@example.com', 'userprofile': None}

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expectedResponse)

    def test_post_not_allowed_to_myurl_endpoint(self):
        response = self.client.post(MY_USER_URL, {})

        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)

    # def test_update_userprofile(self):
    #     """Test update user profile for an authenticated user, should
    #     only update first_name, last_name and image as of now"""
    #     body = {
    #         'email': 'updatedemail@example.com',
    #         'password': 'new_password',
    #         'userprofile': {
    #             'first_name': 'Hans',
    #             'last_name': 'Wurst',
    #             'image': 'https://example.com'
    #         }
    #     }

    #     jsonBody = json.dumps(body, indent=4)
    #     response = self.client.patch(MY_USER_URL,  jsonBody)

    #     # self.user.refresh_from_db()
    #     # self.assertEqual(self.user.email, body['email'])
    #     # self.assertTrue(self.user.check_password(body['password']))
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
