from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    CRUD API for Book resources.
    list, create, retrieve, update, partial_update, destroy.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
