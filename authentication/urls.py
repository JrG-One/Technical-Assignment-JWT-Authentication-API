from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import TokenVerifyView, ValidateTokenView

urlpatterns = [
    # 1. Login → issues access & refresh
    path('login/',   TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # 2. Refresh → rotate tokens
    path('refresh/', TokenRefreshView.as_view(),    name='token_refresh'),
    # 3. Verify → custom verify endpoint
    path('verify/',  TokenVerifyView.as_view(),     name='token_verify'),
    # 4. Validate → protected user info
    path('validate/',ValidateTokenView.as_view(),   name='token_validate'),
]