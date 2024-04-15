from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # 우리가 바꿔야 하는 부분만 재작성하는 거라
        model = get_user_model()
        # get_user_model()
        # : 현재 django 프로젝트에 활성화된 user 객체를 반환하는 함수

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email',)