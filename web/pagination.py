from rest_framework.pagination import PageNumberPagination


class DeafualtPagination(PageNumberPagination):
    page_size = 10