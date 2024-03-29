from django.db import models

# 교재 46p 3번
# def 미디어파일상세경로함수():
#     pass

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    image = models.ImageField(blank=True, upload_to='%Y/%m/%d')
    # blank : 빈 문자열도 저장하도록(이미지 업로드 안 하는 경우도 있으니까)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
