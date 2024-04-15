from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer

@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        # articles가 다중데이터기 때문에 many=True
        return Response(serializer.data)    # serializer는 객체 덩어리라서 .data 필수
    
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)    # 뭘하든 간에 조회가 필요하기 때문에 if 문 밖으로
    if request.method == 'GET':
        serializer = ArticleSerializer(article) # 이건 단일데이터니까 many 옵션 안 씀
        return Response(serializer.data)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        # partial = True로 하지 않으면 제목만 수정하고 싶어도 내용 데이터까지 같이 보내줘야 함
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
