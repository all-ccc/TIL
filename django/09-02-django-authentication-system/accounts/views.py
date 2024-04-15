from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import CustomUserCreationForm, CustomUserChangeForm


# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@login_required
# -> 인증된 사용자만(로그인한 회원) 이 함수를 사용할 수 있도록
def logout(request):
    auth_logout(request)
    return redirect('articles:index')


def signup(request):    # create랑 비슷함
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # 회원가입 후 로그인까지 이어서 진행하려면?
            # user = form.save()
            # auth_login(request, user)
            return redirect('articles:index')

    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)
# UserCreationForm 은 modelForm이라서 인자구성이
# 1) data, 2) files
# 그냥 form 은 1) request, 2) data

@login_required
def delete(request):
    # 삭제하고자 하는 User를 조회 후 삭제할 필요 없다.
    # user 객체는 이미 요청을 하는 데이터 안에 들어있음
    request.user.delete()
    return redirect('articles:index')


@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/update.html', context)


@login_required
def change_password(request, user_pk):
    if request.method == 'POST':
        # PasswordChangeForm은 user, data 순으로 인자 구성
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()     # save를 마치면 비밀번호 변경한 대상을 반환해줌
            # update_session_auth_hash: 암호 변경 시 세션 무효화를 막아주는 함수
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        # PasswordChangeForm은 첫 번째 인자 user가 필수!
        form = PasswordChangeForm(request.user) 
    context = { 
        'form' : form,
    }
    return render(request, 'accounts/change_password.html', context)