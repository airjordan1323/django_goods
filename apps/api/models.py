from django.db import models
from datetime import datetime


class Weather(models.Model):
    # name = models.CharField("Название погоды", max_length=30)
    icon = models.CharField('Иконка', max_length=250)
    temperature = models.SmallIntegerField()
    pub_date = models.DateTimeField("Дата публикации", default=datetime.now,
                                    help_text="Дата когда данные были внесены в базу данных")


    class Meta:
        verbose_name = "Погода"
        verbose_name_plural = "Погода"
        ordering = ['-pub_date']
