# books/models.py

from django.db import models

class ElectronicBook(models.Model):
    TARGET_CHOICES = (
        ('student', 'Ученик'),
        ('teacher', 'Учитель'),
    )

    title = models.CharField("Название", max_length=255)
    author = models.CharField("Автор", max_length=255)
    year = models.PositiveIntegerField("Год")
    grades = models.PositiveIntegerField("Grades", null=True, blank=True)
    target = models.CharField("Для кого", max_length=20, choices=TARGET_CHOICES)
    slug = models.SlugField("Слаг", unique=True)
    file = models.FileField("Файл книги", upload_to='books/')

    def __str__(self):
        return self.title




class BookAudioFile(models.Model):
    AUDIO_TYPE_CHOICES = (
        ('main', 'Основное'),
        ('repeat', 'Повторение'),
    )

    book = models.ForeignKey(ElectronicBook, related_name='audio_files', on_delete=models.CASCADE)
    page = models.IntegerField()
    audio_tag = models.DecimalField(max_digits=3, decimal_places=1)
    order = models.PositiveIntegerField()
    audio_file = models.FileField(upload_to='audios/')
    audio_type = models.CharField(max_length=20, choices=AUDIO_TYPE_CHOICES, default='main')
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.book.title} — Page {self.page}"



