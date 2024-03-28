from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article  # 어떤 모델과 연동?
        # 사용자에게 받아야 하는 값 많다면 아래처럼 써서 전체 필드를 다 받아올 수 있음
        fields = '__all__'