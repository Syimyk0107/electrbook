# books/pagination.py

from rest_framework.pagination import PageNumberPagination

class BookPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'  # если хочешь дать пользователю менять лимит
    max_page_size = 100
