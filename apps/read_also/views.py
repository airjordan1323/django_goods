import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import News
from .serializers import NewsDetailSerializer, NewsListTwoSerializer, NewsListSerializer
from rest_framework.generics import ListAPIView
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


class BigListPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 40


class NewsListView(ListAPIView):
    """вывод список новостей"""
    queryset = News.objects.all()
    serializer_class = NewsListSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.OrderingFilter]


class NewsListTwoView(ListAPIView):
    """вывод список новостей 2"""
    queryset = News.objects.all()
    serializer_class = NewsListTwoSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description', ]


class NewsDetailView(APIView):
    """вывод деталей новостей иногда apiview не показывает полный путь
    к медии надо добавить context={'request': request}"""

    def get(self, request, pk):
        queryset = News.objects.get(id=pk)
        serializer_class = NewsDetailSerializer(queryset, context={'request': request})
        return Response(serializer_class.data)
