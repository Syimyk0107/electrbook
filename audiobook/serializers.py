# books/serializers.py

from rest_framework import serializers
from .models import (ElectronicBook, BookAudioFile)

class BookAudioFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookAudioFile
        fields = '__all__'

class ElectronicBookSerializer(serializers.ModelSerializer):
    audio_files = BookAudioFileSerializer(many=True, read_only=True)

    class Meta:
        model = ElectronicBook

        fields = ['id', 'title', 'author', 'year', 'grades', 'target', 'slug', 'file', 'audio_files']








