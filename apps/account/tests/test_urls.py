from django.urls import resolve

from rest_framework_simplejwt import views as jwt_views

from apps.account import views
from apps.account.tests.test_setup import TestSetup


class TestUrls(TestSetup):
    """Тестирование url адресы"""

    def test_login(self):
        url = self.login_url
        view_class = resolve(url).func.view_class
        return self.assertEqual(view_class, views.LoginAPIView)

    def test_login_refresh(self):
        url = self.refresh_url
        view_class = resolve(url).func.view_class
        return self.assertEqual(view_class, jwt_views.TokenRefreshView)

    def test_sign_up(self):
        url = self.register_url
        view_class = resolve(url).func.view_class
        return self.assertEqual(view_class, views.RegisterView)

