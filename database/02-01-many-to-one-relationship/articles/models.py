from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # ForeignKey 이름은 참조하는 모델 클래스 이름의 단수형으로 작성(나중에 DB에 article_id로 저장됨)
    # on_delete : 게시물 삭제 시 댓글 처리 방법 설정(CASCADE: 댓글도 함께 삭제)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)