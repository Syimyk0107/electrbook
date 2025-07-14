# books/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ElectronicBookViewSet, BookAudioFileViewSet

router = DefaultRouter()
router.register(r'electronic_books', ElectronicBookViewSet)
router.register(r'audio-files', BookAudioFileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
