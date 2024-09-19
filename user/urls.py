from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# urlpatterns = [
#     path('signup/', SignupView.as_view(), name='signup'),
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     path('dj-rest-auth/', include('dj_rest_auth.urls')),
#     path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
#     # path('accounts/google/login/', CustomGoogleLogin.as_view(), name='google-login'),

#     path('accounts/', include('allauth.urls')),
#     # path('accounts/google/login/', GoogleLoginAPIView.as_view(), name='google-login'),
#     # path('accounts/google/login/callbac/', CustomSocialLoginView.as_view(), name='custom_social_login')
# ]


from django.urls import path, include
from .views import RegisterView, VerifyEmail, LoginAPIView

urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
    path('login/',LoginAPIView.as_view(),name='login'),
    path('email-verify/',VerifyEmail.as_view(),name='email-verify'),
    # path('accounts/', include('allauth.urls')),
    # path('accounts/google/login/', GoogleLoginAPIView.as_view(), name='google-login'),
    # path('accounts/google/login/callbac/', CustomSocialLoginView.as_view(), name='custom_social_login')
    

]
