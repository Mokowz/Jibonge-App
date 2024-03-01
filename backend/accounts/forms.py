from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name",]
        exclude = ['date_joined']

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name"]
        exclude = ['date_joined']
