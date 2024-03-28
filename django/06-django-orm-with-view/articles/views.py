from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

# 특정한 번호의 게시글 하나를 조회하는 문법
def detail(request, pk):
    # variable routing 으로 인해 넘어오는 변수는
    # view 함수의 두 번째 인자부터 받을 수 있음 (urls에서 쓴 변수명과 같아야)
    article = Article.objects.get(pk=pk)  # 쿼리셋이 아닌 단일 모델 인스턴스로 받아옴
    # 위의 함수 인자로 들어온 pk가 '=' 다음의 pk로 들어오게 됨
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # print(request.GET) -> <QueryDict: {'title': ['ㅇㄹ'], 'content': ['ㅇㄹ']}>
    title = request.POST.get('title')
    content = request.POST.get('content')    # 예쁘게 할라면 이래 변수 만들어주면 깔끔

    # 방법 3가지
    # 1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2 (이걸 쓰자)
    article = Article(title=title, content=content)
    article.save()

    # 3 (유효성 검증할 타이밍이 X)
    # Article.objects.create(title=title, content=content)
    
    # return render(request, 'articles/create.html')
    # -> create 함수는 페이지를 줄 필요 X, POST로 게시글 작성해줘! 그것만 하면 핵심 로직은 끝

    # 게시글이 작성된 detail 페이지로 사용자를 보낸다
    # return redirect('주소', 파라미터)
    return redirect('articles:detail', article.pk)  # save가 끝난 article에 id가 부여되니까

def delete(request, pk):
    # 몇 번 글 삭제할 건데? (= 조회 필요)
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')   # 메인페이지로 ㄱㄱ

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):    # create와 유사함
    # 몇 번 게시글 수정? -> 조회 필요(create와의 차이점)
    article = Article.objects.get(pk=pk)

    title = request.POST.get('title')
    content = request.POST.get('content')    # 예쁘게 할라면 이래 변수 만들어주면 깔끔

    # article = Article(title=title, content=content) -> 이건 새로운 인스턴스 생성임
    article.title = title
    article.content = content
    article.save()

    return redirect('articles:detail', article.pk) 


