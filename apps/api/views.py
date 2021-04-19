from rest_framework.response import Response
from .serializers import WeatherSerializer
from rest_framework.views import APIView
from datetime import datetime
from .models import Weather
import requests


class WeatherCast(APIView):
    def get(self, request):
        queryset = Weather.objects.all()[:3]
        if len(queryset) == 3:
            item = queryset[0].pub_date
            now = datetime.now()
            if item.year <= now.year and item.day < now.day and item.month <= now.month:
                new_items = get_forecast()
                for dele in queryset:
                    dele.delete()
                for we in new_items:
                    Weather.objects.create(icon=we[1], temperature=we[0])
                queryset = Weather.objects.all()[:3]
        else:
            new_items = get_forecast()
            for we in new_items:
                Weather.objects.create(icon=we[1], temperature=we[0])
            queryset = Weather.objects.all()[:3]

        serializer = WeatherSerializer(queryset, many=True)
        return Response(serializer.data)


def get_forecast():
    url = 'http://api.openweathermap.org/data/2.5/forecast?q=Tashkent&cnt=3&appid=da48613766e09300cf7c0cbeea366629&units=metric'
    res = requests.get(url).json()
    items = []
    for item in res['list']:
        temp = item['main']['temp']
        icon = f"https://openweathermap.org/img/wn/{item['weather'][0]['icon']}@2x.png"
        new_arr = [temp, icon]
        items.append(new_arr)
    return items
