from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm, CommentForm


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    # 특정 게시글에 작성된 모든 댓글 조회(Article -> Comment, 역참조)
    # 역참조대상_set은 objects같은 매니저임~
    comments = article.comment_set.all()
    # DB에 있는 모든 댓글을 조회(특정 게시글에 작성된 모든 댓글 조회가 아님)
    # Comment.objects.all()

    # 사용자로부터 댓글 데이터 입력을 받기 위한 form
     # detail은 지금 form으로 뭘 보내고 이런 게 아님..
    # 폼 자체를 보여주긴 해야하니까 보내는 거임
    comment_form = CommentForm()
    context = {
        'article': article,
        'comments' : comments,
        'comment_form' : comment_form,
    }
    return render(request, 'articles/detail.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@login_required
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)


def comments_create(request, pk):
    # 게시글 조회 (어떤 게시글에 작성되어야 하는지 알아야 하기 때문)
    article = Article.objects.get(pk=pk)
    # 게시글에 작성된 comment들을 받아 옴
    comments = article.comment_set.all()

    # 사용자 입력 데이터를 받아서 Comment 저장 (+ 유효성 저장)
    comment_form = CommentForm(request.POST)

    if comment_form.is_valid():
        # 저장이 이루어지기 전에 comment 인스턴스를 제공받는 게 필요
        # save(commit=False) : DB에 저장하지 않고 인스턴스만 반환
        comment = comment_form.save(commit=False)
        comment.article = article   # 어떤 게시글인지 넣어주고
        comment.save()      # 진짜로 저장
        return redirect('articles:detail', article.pk)
    
    # 무조건 post로 받기 때문에 else고 뭐고 할 게 없음

    # 현재! 댓글폼에 작성된 게 없다면~ 그냥 지금 가지고 있는 context로 detail.html 랜더링하는데,,
    # form 자체를 화면에 보여주긴 해야하니까 같이 context로 보냄
    context = {
        'comment_form' : comment_form,
        'article' : article,
        'comments' : comments,
    }
    return render(request, 'articles/detail.html', context)


def comments_delete(reqeust, article_pk, comment_pk):
    # 어떤 댓글을 삭제하는지 조회 
    comment = Comment.objects.get(pk=comment_pk)
    # 아래 코드처럼 작성 가능
    # 단, 이렇게 작성할 경우 url에서 article_pk가 제거되고 url 구성을 변경해야 함
    # 지금까지의 url 전체 구성 및 통일성을 유지하기 위해 아래 코드 방식을 선택하지 않음
    # article_pk = comment.article.pk
    comment.delete()
    return redirect('articles:detail', article_pk)