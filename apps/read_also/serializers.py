from rest_framework import serializers
from .models import News, Category


class CategorySerializer(serializers.ModelSerializer):
    """Список категорий"""

    class Meta:
        model = Category
        fields = 'id', 'name',


class NewsReadAlsoSerializer(serializers.ModelSerializer):
    """Read also новостей"""
    category = CategorySerializer()

    class Meta:
        model = News
        fields = ('id', 'title', 'category', 'image', 'pub_date',
                  'last_change',)


class NewsListSerializer(serializers.ModelSerializer):
    """Список новостей с read also"""
    category = CategorySerializer()
    read_also = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ('id', 'title', 'category', 'image', 'pub_date',
                  'last_change', 'read_also')

    def get_read_also(self, obj):
        read_list = News.objects.filter(category__id=obj.category.id).exclude(id=obj.id).order_by('-pub_date')[:2]
        serializer = NewsReadAlsoSerializer(read_list, many=True, context=self.context)
        return serializer.data


class NewsListTwoSerializer(serializers.ModelSerializer):
    """Список новостей без read also"""
    category = CategorySerializer()

    class Meta:
        model = News
        fields = ('id', 'title', 'category', 'image', 'pub_date',
                  'last_change',)


class NewsDetailSerializer(serializers.ModelSerializer):
    """Детальные новости"""
    category = CategorySerializer()
    read_also = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ('id', 'title', 'description', 'category', 'image', 'pub_date',
                  'last_change', 'read_also')

    def get_read_also(self, obj):
        read_list = News.objects.filter(category__id=obj.category.id).exclude(id=obj.id).order_by('-pub_date')[:4]
        serializer = NewsReadAlsoSerializer(read_list, many=True, context=self.context)
        return serializer.data
