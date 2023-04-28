from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms    # 追記


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', 'age')

# ここから
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
            'age',
        )
# ここまで