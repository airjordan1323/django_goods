from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class NewsAdminForm(forms.ModelForm):
    description_ru = forms.CharField(label="Описание", widget=CKEditorUploadingWidget)
    description_en = forms.CharField(label="Description", widget=CKEditorUploadingWidget, required=False)
    description_uz = forms.CharField(label="Tavsif", widget=CKEditorUploadingWidget, required=False)


class HistoryAdminForm(forms.ModelForm):
    description_ru = forms.CharField(label="Описание", widget=CKEditorUploadingWidget)
    description_en = forms.CharField(label="Description", widget=CKEditorUploadingWidget, required=False)
    description_uz = forms.CharField(label="Tavsif", widget=CKEditorUploadingWidget, required=False)


# TODO READONLY FIELD MUST BE pub_date IF ADD last_change
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = 'title',
    list_filter = ('pub_date',)
    search_fields = ('id', 'date')
    save_on_top = True
    save_as = True
    form = NewsAdminForm


@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = 'name',


@admin.register(Sponsors)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = 'name',


@admin.register(Movies)
class CastsAdmin(TranslationAdmin):
    list_display = ("id", "title")
    list_display_links = 'title',


@admin.register(History)
class HistoryAdmin(TranslationAdmin):
    list_display = ("id", "year")
    list_display_links = 'year',
    form = HistoryAdminForm


@admin.register(Media)
class MediaAdmin(TranslationAdmin):
    list_display = ("id", "date")
    list_display_links = 'date',


@admin.register(Location)
class MediaAdmin(TranslationAdmin):
    list_display = ("id", "name")
    list_display_links = 'name',
    filter_horizontal = ('gallery',)


@admin.register(Guests)
class MediaAdmin(TranslationAdmin):
    list_display = ("id", "fio")
    list_display_links = 'fio',


@admin.register(Contact)
class MediaAdmin(admin.ModelAdmin):
    list_display = ("id", "fio")
    list_display_links = 'fio',
    readonly_fields = 'fio', 'position', 'phone', 'email', 'message'


admin.site.register(Gallery)
admin.site.register(Day)
