from datetime import datetime
from django.urls import reverse
from django.db import models


class News(models.Model):
    title = models.CharField("Оглавление", max_length=300)
    description = models.TextField("Описание")
    image = models.ImageField("Картинка", upload_to='images/')
    pub_date = models.DateTimeField("Дата публикации", default=datetime.now,
                                    help_text="Дата когда данные были внесены в базу данных")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"
        ordering = ['-pub_date']


class History(models.Model):
    title = models.CharField("Оглавление", max_length=300)
    description = models.TextField("Описание", max_length=5000)
    year = models.CharField("Год", max_length=15)
    image = models.ImageField("Картинка", upload_to='history/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "История"
        verbose_name_plural = "Истории"
        ordering = ['-year']


class Partners(models.Model):
    name = models.CharField("Название организации", max_length=200)
    image = models.ImageField("Логотип организации", upload_to='partners/')
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Партнер"
        verbose_name_plural = "Партнеры"


class Sponsors(models.Model):
    name = models.CharField("Название организации", max_length=200)
    image = models.ImageField("Логотип организации", upload_to='sponsors/')
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Спонсор"
        verbose_name_plural = "Спонсоры"


class Media(models.Model):
    date = models.DateField("Дата материала", auto_now_add=True)
    title = models.CharField("Название медии", max_length=100, blank=True, null=True)
    file = models.ImageField("Медия", upload_to='gallery/')
    link = models.URLField("Ссылка на ютуб", null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.date}"

    class Meta:
        verbose_name = "Медиа"
        verbose_name_plural = "Медии"
        ordering = ['-id']


class Movies(models.Model):
    TYPE_CHOICES = (
        ('Retrospective', 'Retrospective'),
        ('Young', 'Young')
    )
    title = models.CharField("Название фильма", max_length=150)
    poster = models.ImageField("Постер фильма", upload_to='poster/')
    author = models.CharField("Автор", max_length=100)
    year = models.CharField("Год", max_length=10)
    type = models.CharField("Тип", max_length=50, choices=TYPE_CHOICES)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кинофильм"
        verbose_name_plural = "Кинофильмы"


class Gallery(models.Model):
    image = models.ImageField("Фото", upload_to='gallery/')

    def __str__(self):
        return f"{self.image}"

    class Meta:
        verbose_name = "Галлерея"
        verbose_name_plural = "Галлерея"


class Location(models.Model):
    name = models.CharField("Название Города", max_length=50)
    description = models.TextField("Описание", max_length=500)
    date = models.DateField("Дата", default=datetime.now)
    gallery = models.ManyToManyField(Gallery, verbose_name="Фотографии городов")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"


class Day(models.Model):
    file = models.FileField("Файл", upload_to='files/')

    def __str__(self):
        return f"{self.file}"

    class Meta:
        verbose_name_plural = "Файлы"
        verbose_name = "Файл"


class Guests(models.Model):
    fio = models.CharField("Фимилия Имя гостя", max_length=150)
    position = models.CharField("Должность", max_length=50)
    photo = models.ImageField("Фотографии", upload_to='personal/')
    link = models.URLField("Ссылка на страницу гостя")

    def __str__(self):
        return f"{self.fio} - {self.position}"

    class Meta:
        verbose_name_plural = "Гости"
        verbose_name = "Гость"


class Contact(models.Model):
    fio = models.CharField("Ф.И.О", max_length=200)
    position = models.CharField("Должность", max_length=70)
    phone = models.CharField("Телефон", max_length=14)
    email = models.EmailField("Электронная почта")
    message = models.TextField("Сообщение")

    def __str__(self):
        return f"{self.fio} - {self.position} -{self.phone}"

    class Meta:
        verbose_name_plural = "Контакт"
        verbose_name = "Контакты"
