from django.urls import path, include
# from .views import CustomUserRegistrationView

urlpatterns = [
    path('accounts/', include('dj_rest_auth.urls')),
    # path('accounts/registration/', include('dj_rest_auth.urls'))
    # path('accounts/registration/', include('dj_rest_auth.registration.urls')),
    # path('accounts/registration/', CustomUserRegistrationView.as_view(), name='user_registration'),
]