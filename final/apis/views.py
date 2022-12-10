from rest_framework.decorators import api_view
from rest_framework.response import Response
from books.models import Book
from .serializers import BookSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET/api',
        'GET/api/books',
        'GET/api/book/:id'
    ]
    return Response(routes)


@api_view(['GET'])
def getBooks(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getBook(request, id):
    b = Book.objects.get(id=id)
    serializer = BookSerializer(b, many=False)
    return Response(serializer.data)
