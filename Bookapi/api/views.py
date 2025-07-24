from rest_framework import viewsets
from api.models import Book
from.Serializer import BookSrrializers



# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSrrializers

