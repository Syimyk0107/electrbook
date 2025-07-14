# books/admin.py

from django.contrib import admin
from django.utils.html import format_html
from .models import ElectronicBook, BookAudioFile

@admin.register(BookAudioFile)
class BookAudioFileAdmin(admin.ModelAdmin):
    list_display = [
        'book', 'page', 'audio_tag', 'order',
        'audio_player', 'audio_type', 'description'
    ]
    list_filter = ['book', 'page', 'audio_type']

    def audio_player(self, obj):
        if obj.audio_file:
            return format_html(
                '<audio controls preload="none" style="max-width:200px;">'
                '<source src="{}" type="audio/mpeg">'
                'Your browser does not support the audio tag.'
                '</audio>',
                obj.audio_file.url
            )
        return "No audio file"

    audio_player.short_description = "Аудио"
# books/admin.py

@admin.register(ElectronicBook)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'year', 'grades', 'target', 'slug', 'file_link']
    list_filter = ['year', 'target','title']
    search_fields = ['title', 'author']

    def file_link(self, obj):
        if obj.file:
            return f"<a href='{obj.file.url}' target='_blank'>Скачать</a>"
        return "Нет файла"
    file_link.allow_tags = True
    file_link.short_description = "Файл"
