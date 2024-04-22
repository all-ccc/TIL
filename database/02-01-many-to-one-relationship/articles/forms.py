from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # '__all__' : 입력 데이터가 필요한 모든 필드
        # fields = '__all__'
        fields = ('content',)
        # Article은 댓글이 생성될 때 사용하는 view 함수에서 넣어줘야 함

