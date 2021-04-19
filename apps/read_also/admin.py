from ckeditor_uploader.widgets import CKEditorUploadingWidget
from modeltranslation.admin import TranslationAdmin
from rangefilter.filter import DateRangeFilter
from .models import News, Category
from django.contrib import admin
from django import forms


class NewsAdminForm(forms.ModelForm):
    description_ru = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
    description_en = forms.CharField(label="Description", widget=CKEditorUploadingWidget(), required=False)


@admin.register(News)
class NewsAdmin(TranslationAdmin):
    list_display = ("id", "title")
    list_display_links = 'title',
    list_filter = (
        ('pub_date', DateRangeFilter),
    )
    search_fields = ('id', 'pub_date')
    form = NewsAdminForm
    save_on_top = True
    save_as = True


admin.site.register(Category)
