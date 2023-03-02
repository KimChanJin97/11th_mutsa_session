from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def _create_user(self, username, password, **kwargs): # _: 외부에서 직접 접근하지 않겠다는 관습
        user = self.model(username = username, **kwargs)
        user.set_password(password)
        user.save()

    def create_user(self, username, password, **kwargs):
        self._create_user(username, password, **kwargs) # 여기서 _create_user 사용

    def create_superuser(self, username, password, **kwargs):
        kwargs.setdefault("is_superuser", True)
        self._create_user(username, password, **kwargs) # 여기서 _create_user 사용

class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'username'

    username = models.CharField(unique=True, max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    @property
    def is_staff(self):
        return self.is_superuser