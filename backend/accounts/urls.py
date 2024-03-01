from django.urls import path, include
from .views import CustomRegistrationView

urlpatterns = [
    path('accounts/', include('dj_rest_auth.urls')),
    path('accounts/registration/', CustomRegistrationView.as_view(), name='user_registration'),
]