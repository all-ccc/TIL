from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Book
from .serializers import BookListSerializer, BookSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':  # 도서 생성
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE',])
def book_detail(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':    # 도서 삭제
        book.delete()
        
        error_dict = {
            'delete' : '도서 고유 번호 ' + book.isbn + '번의 ' + book.title + '을 삭제하였습니다.'
        }
        return Response(error_dict)


