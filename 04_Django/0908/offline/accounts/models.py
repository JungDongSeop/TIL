from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# 내가 필드 다 만들 거 아님
# django의 유저 모델 상속받아서 사용
class User(AbstractUser):
    pass