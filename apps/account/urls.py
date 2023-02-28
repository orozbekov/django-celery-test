from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from apps.account.views import RegisterView, activate_view, LoginAPIView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('activate/<str:activation_code>/', activate_view, name='activate-email'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]