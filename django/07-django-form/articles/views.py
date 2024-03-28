from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


# def new(request):
#     form = ArticleForm()
#     context = {
#         'form' : form,
#     }
#     return render(request, 'articles/new.html', context)


# def create(request):
#     # title = request.POST.get('title')
#     # content = request.POST.get('content')
#     # article = Article(title=title, content=content)
#     # article.save()
#     form = ArticleForm(request.POST)    # title, content가 이렇게 한 방에
#     if form.is_valid():  # 유효성 검사 통과한다면
#         form.save()
#         return redirect('articles:detail')
    
#     # if 통과하지 못하면 여기로 옴 (+ 실패한 이유와 함께.. 그래서 처음의 form과 다름)
#     context = {
#         'form' : form,
#     }
#     # new 템플릿 다시 줌(첨의 form과 != 때문)
#     # render : 에러가 담긴 폼을 새로운 템플릿에 만들어서 응답을 하는 것
#     return render(request, 'articles/new.html', context) 
#     # return redirect('articles:new')
#     # redirect 안되는 이유
#     # - redirect = 사용자한테 너 new 주소로 다시 요청을 보내 (new 함수가 실행되어 에러메시지를 볼 수 없음)

# new() + create()
def create(request):
    form = ArticleForm(request.POST)
    if request.method == 'POST':    # POST -> DB 조작하는 부분임(그래서 POST 먼저 확인)
        if form.is_valid():         # create 함수
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:  # POST가 아닌 모든 경우        # new 함수
        form = ArticleForm()
    # context 위치가 여기인 이유 : create, new에서 is.valid 통과 못 한 두 경우 다 처리 가능
    context = {     
        'form' : form,
    }
    return render(request, 'articles/create.html', context)



def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     # instance라는 키워드 인자에 조회한 객체를 넣어줌 -> 원래 작성한 내용 보여주기 위해서
#     form = ArticleForm(instance=article)
#     context = {
#         'article': article,
#         'form' : form,
#     }
#     return render(request, 'articles/edit.html', context)


# def update(request, pk):
#     # title = request.POST.get('title')
#     # content = request.POST.get('content')
#     # article.title = title
#     # article.content = content
#     # article.save()

#     article = Article.objects.get(pk=pk)
#     # instance 키워드로 기존 객체를 넣어줘야 새로 생성이 아니고!! 수정이구나 인식함
#     form = ArticleForm(request.POST, instance=article) 
#     if form.is_valid():

#         form.save()
#         return redirect('articles:detail', article.pk)
#     context = {
#         'form' : form,
#         'article' : article,    # 이거 안 적으면 pk 없어서 에러남
#     }
#     return render(request, 'articles/edit.html', context)

# update() + edit()
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':        # update()  
        form = ArticleForm(request.POST, instance=article) 
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:   # edit()
        form = ArticleForm(instance=article)
    context = {
        'form' : form,
        'article' : article,    
    }
    return render(request, 'articles/edit.html', context)