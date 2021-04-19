from django.db import models
from datetime import datetime


class Category(models.Model):
    name = models.CharField("Название Категории", max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class News(models.Model):
    title = models.CharField("Оглавление", max_length=150)
    description = models.TextField("Описание")
    category = models.ForeignKey(Category, verbose_name="Категория Новости",
                                 on_delete=models.CASCADE)
    image = models.ImageField("Картинка", upload_to='images/')
    pub_date = models.DateTimeField("Дата публикации", default=datetime.now,
                                    help_text="Дата когда данные были внесены в базу данных")
    last_change = models.DateTimeField("Дата изменении", auto_now_add=True,
                                       help_text="Дата последней изменении из базы данных")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"
