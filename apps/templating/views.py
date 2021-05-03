from django.template.defaultfilters import register
from django.views.generic.base import View
from django.shortcuts import render
from .models import *
from django import template
from django.urls import resolve, reverse
from django.utils import translation
from .forms import ContactForm

"""Возможность изменений url находясь на текущей странице через темплейты"""


class TranslatedURL(template.Node):
    def __init__(self, language):
        self.language = language

    def render(self, context):
        view = resolve(context['request'].path)
        request_language = translation.get_language()
        translation.activate(self.language)
        url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        translation.activate(request_language)
        return url


@register.tag(name='translate_url')
def do_translate_url(parser, token):
    language = token.split_contents()[1]
    return TranslatedURL(language)


"""декоратор чтобы брать какую то часть из данных из бд"""


@register.filter(name="firstChar")
def firstChar(value):
    return value[:1]


@register.filter(name="elseChars")
def elseChars(value):
    return value[1:]


"""Берет последнее после двух слово"""


@register.filter(name="twoChars")
def twoChars(value):
    return value[2:]


@register.filter(name="twoChar")
def twoChar(value):
    return value[:2]


"""Берет первое слово"""


@register.filter(name="firstWord")
def firstWord(value):
    return value.split()[0]


"""Берет первое слово"""


@register.filter(name="elseWord")
def elseWord(value):
    return value.partition(' ')[2]


"""Берет первый 500 слов"""


@register.filter(name="firstHundred")
def firstHundred(value, indexes):
    try:
        end_index = int(indexes.split()[1])
        start_index = int(indexes.split()[0])
        return value[start_index:end_index]
    except Exception as e:
        start_index = int(indexes.split()[0])
        return value[start_index:]


@register.filter(name="wordsLimit")
def wordsLimit(value, indexes):
    new_list = [' '.join(item.split()[:indexes]) for item in [value] if item]
    return ' '.join(word[0] for word in [new_list])


@register.filter(name="else_words_limit")
def else_words_limit(value, indexes):
    return ' '.join(word for word in value.split()[indexes:])


"""Берет первый 500 слов"""


@register.filter(name="elseHundred")
def elseHundred(value):
    return value.partition(' ')[499]


# @register.filter(name="thirdWord")
# def thirdWord(value):
#     return value[1:]


##########################################################


class NewsListView(View):
    def get(self, request):
        news = News.objects.all()
        return render(request, "news.html", {"news_list": news})


class MovieListView(View):
    def get(self, request):
        retro = Movies.objects.filter(type="Retrospective")
        young = Movies.objects.filter(type="Young")
        return render(request, "retro.html", {"retro_list": retro, "young_list": young})


class MediaListView(View):
    def get(self, request):
        media = Media.objects.all()
        return render(request, "media.html", {"media_list": media})


class LocationView(View):
    def get(self, request):
        return render(request, "locations.html", {"location_list": Location.objects.all()})


class HistoryView(View):
    def get(self, request):
        history = History.objects.all()
        return render(request, "history.html", {"history_list": history})


class DayView(View):
    def get(self, request):
        day = Day.objects.all()
        return render(request, "press.html", {"press_list": day})


class GuestsAndPartnersView(View):
    def get(self, request):
        guests = Guests.objects.all()
        partners = Partners.objects.all()
        media = Media.objects.all()[:4]
        sponsors = Sponsors.objects.all()
        form = ContactForm(None)
        return render(request, "index.html", {"guests_list": guests,
                                              "partners_list": partners,
                                              "sponsors_list": sponsors,
                                              "media_list": media,
                                              "form": form})

    def post(self, request):
        error = ''
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = ContactForm()
        data = {
            'form': form,
            'error': error
        }
        return render(request, 'index.html', data)


def kino(request):
    return render(request, "kino.html")
