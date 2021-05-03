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


# class OrderListView(generics.ListAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#
#
# class OrderNullView(APIView):
#     parser_classes = [JSONParser]
#
#     def post(self, request):
#         freq = {}
#         for i in request.data['items']:
#             if i['id'] in freq:
#                 freq[i['id']] += 1
#             else:
#                 freq[i['id']] = 1
#
#         try:
#             order = Order.objects.create(type_dj="NULL", author=request.user, name=request.data['name'],
#                                          phone=request.data['phone'],)
#             for item_id, count in freq.items():
#                 item = Item.objects.get(id=item_id)
#                 item.count -= count
#                 item.save()
#                 count_item = CountItems.objects.create(item=item, count=count)
#                 order.items.add(count_item)
#             return Response({"status": "added"}, status=201)
#         except Exception as e:
#             return Response({"status": str(e)}, status=500)
#
#
# class OrderUpdateView(APIView):
#     def get(self, request, pk, action):
#         order = Order.objects.get(id=pk)
#         if action == "accept":
#             order.type_dj = "ACCEPTED"
#             order.save()
#             trans = Transaction(author=request.user, type="INCOME", sum=0)
#             final = 0
#             count_items = []
#             for item in order.items.all():
#                 final += item.item.count * item.item.price
#                 count_items.append(item.item.id)
#             trans.sum = final
#             trans.save()
#             for id in count_items:
#                 trans.items.add(id)
#             return Response(TransactionSerializer(trans).data)
#         elif action == "reject":
#             pass
#         else:
#             return Response({'error': "Unknown action, try using accept or reject"})


# class BuySilkView(APIView):
#     def post(self, request):
#         try:
#             transaction = Transaction.objects.create(name=request.data['name'],
#                                                      phone=request.data['phone'],
#                                                      email=request.data['email'],
#                                                      )
#             for i in request.data['books']:
#                 book = Book.objects.get(id=i['id'])
#                 quantity = i['count']
#                 count_item = CountBook.objects.create(book=book, count=quantity)
#                 transaction.books.add(count_item)
#             return Response({"status": "added"}, status=201)
#         except Exception as e:
#             return Response({"status": e}, status=500)

# in raw method write this json:
# {
#     "name": "иванов иван",
#     "phone": "+9999999999",
#     "email": "bla@bla.com",
#     "books": [
#         {
#             "id": 1,
#             "count": 3
#         },
#         {
#             "id": 2,
#             "count": 12
#         }
#     ]
# }
