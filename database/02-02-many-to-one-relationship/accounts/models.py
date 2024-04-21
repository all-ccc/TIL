from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

    # def __str__(self):
    #     return self.username
    # -> 이 함수가 AbstractUser에 있어서
    # index.html에서 article.user 라고만 써도 username이 출력됨
