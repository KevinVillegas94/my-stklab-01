from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns += [
    path('api/v1/auth/', include([
        path('token/', TokenObtainPairView.as_view(), name='token_obtain'),
        path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ]))
]