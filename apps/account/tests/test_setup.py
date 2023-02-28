from django.urls import reverse
from rest_framework.test import APITestCase


class TestSetup(APITestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.activate_email_url = reverse('activate-email', args=['q63YWee4'])
        self.login_url = reverse('login')
        self.refresh_url = reverse('token-refresh')

        self.user_data = {
            'first_name': 'John',
            'last_name': 'Dich',
            'email': 'john@example.com',
            'password': 'qwertyuiop889',
            'password2': 'qwertyuiop889',
            'user_type': 'admin',
        }

        self.user_login = {
            'email': 'john@example.com',
            'password': 'qwertyuiop889'
        }
        return super().setUp()

    def tearDown(self):
        return super().tearDown()