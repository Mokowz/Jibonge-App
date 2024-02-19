from django.urls import path, include

urlpatterns = [
    path('accounts/', include('dj_rest_auth.urls'))
]