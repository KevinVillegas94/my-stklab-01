from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path, include
from ratelimit.decorators import ratelimit

urlpatterns = [
    path('api/v1/auth/', include([
        path('token/', ratelimit(key='ip', rate='5/h')(TokenObtainPairView.as_view()), name='token_obtain'),
        path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ])),
    # ... tus otras URLs ...
]