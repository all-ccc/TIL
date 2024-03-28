from django import forms
from .models import Article

# class ArticleForm(forms.Form):  # forms라는 모듈에 Form이라는 클래스 상속 받음
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea) # Form 필드에서는 max_length가 필수 아닌 듯


# 만약 사용자 입력 데이터가 많은 모델이라면
# 여기서도 똑같이 대응해야 함 (-> 똑같은 일 반복되는..)
# models 에 쓴 정보를 자동으로 읽어올 수 있는 거 없을까? ==> 그게 바로 ModelForm
class ArticleForm(forms.ModelForm):
    # 제목을 쓰는 부분에 클래스를 넣고 싶다하면 이래 만들어줘야 함
    title = forms.CharField(    
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class' : 'my-title',
            }
        )
    )
    class Meta:
        model = Article  # 어떤 모델과 연동?
        # fields = ('title', 'content')  # 그 모델에서 어떤 필드를 쓸지?
        # 사용자에게 받아야 하는 값 많다면 아래처럼 써서 전체 필드를 다 받아올 수 있음
        fields = '__all__'
        # exclude = ('title',)