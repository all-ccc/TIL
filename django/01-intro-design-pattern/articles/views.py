from django.shortcuts import render

# Create your views here.
# 메인 페이지를 만드는 index라는 이름의 함수를 작성
def index(request):
    # 왜요?
    # render 함수가 그렇게 만들어져 있습니다.
    # render(요청객체, 템플릿경로)
    return render(request, 'index.html') # '' 안에는 templates 폴더 이후의 경로를 쓴 거임