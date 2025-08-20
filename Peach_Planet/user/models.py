from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, user_id, nickname, password=None, **extra_fields):
        if not user_id:
            raise ValueError("user_id는 반드시 입력해야 합니다.")
        user = self.model(user_id=user_id, nickname=nickname, **extra_fields)
        user.set_password(password)  # 비번 해싱
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, nickname, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(user_id, nickname, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    user_id = models.CharField(max_length=30, unique=True)
    nickname = models.CharField(max_length=300, unique=True)

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['nickname']

    objects = CustomUserManager()   # ✅ 반드시 추가
