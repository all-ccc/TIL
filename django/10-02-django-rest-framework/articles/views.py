from rest_framework.response import Response
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from .models import Article, Comment


@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        # articles = Article.objects.all()
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(
            article, data=request.data, partial=True
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def comment_list(request):
    # 전체 댓글 조회
    # comments = Comment.objects.all()
    comments = get_list_or_404(Comment)
    # 직렬화 진행
    serializer = CommentSerializer(comments, many=True) # 첫번째 인자가 QuerySet이면 무조건 many=True 해줘야 함!!
    return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    # 단일 댓글 조회 -> 이건 공통적으로 하니까 if문 위로 올림
    # comment = Comment.objects.get(pk=comment_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        # 직렬화 직행
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)  # 사용자의 데이터를 받아서 직렬화 진행
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # 여기서는 article 안 넣어줘도 되는 이유
            # 처음 작성하는 거 아니라서 comment에 article 데이터가 있음
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        


@api_view(['POST'])
def comment_create(request, article_pk):
    # 게시글 조회
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    # 사용자 입력 데이터를 받아 직렬화 진행
    serializer = CommentSerializer(data=request.data)
    # 유효성 검사
    if serializer.is_valid(raise_exception=True):
        # read_only_fields 작성 안 했을 때는 계속 is_valid에서 걸림 => status 400
        # article이 누락됐다고 판단하기 때문... (유효성 검사 후 article 넣어주니까)
        serializer.save(article=article)   # 여기는 modelForm과 달리 commit 이라는 옵션이 없음
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # raise_exception=True 를 하면 위 코드 생략 가능