from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from .serializers import TransactionSerializer, TransactionPostSerializer
from rest_framework.generics import ListAPIView, CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Transaction, Item
from rest_framework import filters


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 10000
    page_size_query_param = 'page_size'
    max_page_size = 10000


class TransListView(ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['id', 'name']
    ordering_fields = ['id', 'author', 'name', 'pub_date']
    filterset_fields = ['type']

    def get_queryset(self):
        date_from = self.request.query_params.get('from')
        date_to = self.request.query_params.get('to')
        if date_from and date_to:
            return Transaction.objects.filter(pub_date__range=[date_from, date_to])
        else:
            return Transaction.objects.all()


class TransPostView(CreateAPIView):
    """Автоматически добавляет автора в созданный товар"""
    serializer_class = TransactionPostSerializer

    def get_author(self, serializer):
        return serializer.save(author=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.get_author(serializer)
        return Response(TransactionSerializer(instance).data)


class BuyView(APIView):
    """Через raw поле можно отправить данные которые динамический пересчитывает"""
    parser_classes = [JSONParser]

    def post(self, request):
        """
            :param request:
            :return:
        """
        final = 0
        freq = {}
        for i in request.data['items']:
            final += i['price']
            if i['id'] in freq:
                freq[i['id']] += 1
            else:
                freq[i['id']] = 1

        try:
            transaction = Transaction.objects.create(author=request.user, type="INCOME", sum=final)
            for item_id, count in freq.items():
                item = Item.objects.get(id=item_id)
                item.count -= count
                item.save()
                transaction.items.add(item_id)
            return Response({"status": "added"}, status=201)
        except Exception as e:
            return Response({"status": e}, status=500)