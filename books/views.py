from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

@swagger_auto_schema(
    methods=['GET', 'POST'],
    operation_summary='List all authors or create a new author.',
    responses={
        200: openapi.Response('List of authors', AuthorSerializer(many=True)),
        201: openapi.Response('Created author', AuthorSerializer()),
        400: 'Bad request'
    }
)
@api_view(['GET', 'POST'])
def author_list(request):
    """
    List all authors or create a new author.
    """
    if request.method == 'GET':
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    methods=['GET', 'PUT', 'DELETE'],
    operation_summary='Retrieve, update or delete an author instance.',
    responses={
        200: openapi.Response('Author details', AuthorSerializer()),
        204: 'No content',
        404: 'Not found'
    }
)
@api_view(['GET', 'PUT', 'DELETE'])
def author_detail(request, pk):
    """
    Retrieve, update or delete an author instance.
    """
    try:
        author = Author.objects.get(pk=pk)
    except Author.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@swagger_auto_schema(
    methods=['GET', 'POST'],
    operation_summary='List all books or create a new book.',
    responses={
        200: openapi.Response('List of books', BookSerializer(many=True)),
        201: openapi.Response('Created book', BookSerializer()),
        400: 'Bad request'
    }
)
@api_view(['GET', 'POST'])
def book_list(request):
    """
    List all books or create a new book.
    """
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    methods=['GET', 'PUT', 'DELETE'],
    operation_summary='Retrieve, update or delete a book instance.',
    responses={
        200: openapi.Response('Book details', BookSerializer()),
        204: 'No content',
        404: 'Not found'
    }
)
@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, pk):
    """
    Retrieve, update or delete a book instance.
    """
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
