# books/views.py
from rest_framework import viewsets
from .models import ElectronicBook, BookAudioFile
from .serializers import ElectronicBookSerializer, BookAudioFileSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import BookPagination

class ElectronicBookViewSet(viewsets.ModelViewSet):
    queryset = ElectronicBook.objects.all()
    serializer_class = ElectronicBookSerializer

class BookAudioFileViewSet(viewsets.ModelViewSet):
    queryset = BookAudioFile.objects.all()
    serializer_class = BookAudioFileSerializer



# books/views.py


class ElectronicBookViewSet(viewsets.ModelViewSet):
    queryset = ElectronicBook.objects.all()
    serializer_class = ElectronicBookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'title', 'author', 'year', 'grades']
    pagination_class = BookPagination

class BookAudioFileViewSet(viewsets.ModelViewSet):
    queryset = BookAudioFile.objects.all()
    serializer_class = BookAudioFileSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'title', 'author', 'year', 'grades', 'target']
