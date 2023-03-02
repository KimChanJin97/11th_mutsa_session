from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

# 회원가입 폼
class UserRegistraionForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username']

# 로그인(인증) 폼
class UserConfirmationForm(AuthenticationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username']
