from django.db import models

# Create your models here.
class Article(models.Model):    # Model 클래스를 상속받음
    # title, content => 필드(열) 이름
    # .CharField() 이런 거 => 데이터 타입 
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now=True)

# 최종 테이블 이름은 "앱이름_모델클래스이름"으로 합성해서 만듦