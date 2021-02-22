from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm

User = get_user_model()


class UserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name")
