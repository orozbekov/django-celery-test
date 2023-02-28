from rest_framework.test import APITestCase
from apps.account.tests.test_setup import TestSetup
from django.test import override_settings
from apps.account.models import CustomUser


@override_settings(CELERY_TASK_ALWAYS_EAGER=True)
class TestSetup(TestSetup):

    def test_user_registration_with_correct_data(self):
        response = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_user_registration_with_invalid_data(self):
        response = self.client.post(self.register_url)
        self.assertEqual(response.status_code, 400)

    def test_user_can_login_after_verification_and_refresh(self):
        self.client.post(self.register_url, self.user_data, format='json')
        email = self.user_data['email']
        user = CustomUser.objects.get(email=email)
        user.is_active = True
        user.save()
        response = self.client.post(self.login_url, self.user_login)
        self.assertEqual(response.status_code, 200)
        tokens = response.data['tokens']
        self.assertIn('refresh', tokens)
        self.assertIn('access', tokens)

        refresh = {
            'refresh': tokens.get('refresh')
        }
        result = self.client.post(self.refresh_url, refresh)
        self.assertEqual(result.status_code, 200)
        self.assertIn('access', result.data)

    def test_user_cannot_login_with_unverified_email(self):
        self.client.post(self.register_url, self.user_data)
        response = self.client.post(self.login_url, self.user_data)
        self.assertEqual(response.status_code, 401)

