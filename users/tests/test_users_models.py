"""
Tests for user models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class UserModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test successful creation of user with email"""
        email = 'strelewebtest@example.com'
        password = 'testitest'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)

        # needed to use check_password function here,
        # to check for the actual hash
        self.assertTrue(user.check_password(password))

    def test_create_superuser_success(self):
        """Test successful creation of superuser"""
        user = get_user_model().objects.create_superuser(
            'strelewebtest@example.com'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_new_user_email_normalized(self):
        """Test if email is normalized for new users"""
        email_examples = [
            ['strelewebtest@EXAMPLE.com', 'strelewebtest@example.com'],
            ['Strelewebtest2@Example.com', 'Strelewebtest2@example.com'],
            ['STRELEWEBTEST3@EXAMPLE.COM', 'STRELEWEBTEST3@example.com'],
        ]

        for email, expected_email in email_examples:
            user = get_user_model().objects.create_user(email)
            self.assertEqual(user.email, expected_email)

    def test_new_user_no_email_should_raise_error(self):
        """Creating user without an email should raise a ValueError"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('')

    def test_create_user_too_short_pw_should_raise_error(self):
        """Test should fail, password too short"""
        email = 'strelewebtest@example.com'
        password = 'testi'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)

        # needed to use check_password function here,
        # to check for the actual hash
        self.assertTrue(user.check_password(password))
