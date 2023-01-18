from django.db import models
from django.urls import reverse

class Game(models.Model):
    title = models.CharField(max_length = 255,verbose_name = "Название игры")
    content = models.TextField(blank = True, verbose_name = "Описание игры")
    photo = models.ImageField(upload_to = "photos/%Y/%m/%d/", verbose_name = "Фото")
    buy = models.CharField(max_length = 255, verbose_name = "Купить игру")
    pixel = models.BooleanField(default = True)
    best = models.ForeignKey('Best', on_delete = models.PROTECT, null = True, blank=True, verbose_name = "Лучшая")
    janr = models.ForeignKey('Janr', on_delete = models.PROTECT, null = True, blank=True, verbose_name = "Жанр")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Игры'
        verbose_name_plural = 'Игры'


class Best(models.Model):
    name = models.CharField(max_length = 255, verbose_name = "Год лучшее")
    content = models.TextField(blank = True, verbose_name = "Описание года")
    photo = models.ImageField(upload_to = "photos/%Y/%m/%d/", verbose_name = "Фото")
    time_create = models.DateTimeField(auto_now_add = True, verbose_name = "Время создания")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Лучшее'
        verbose_name_plural = 'Лучшее'

    def get_absolute_url(self):
        return reverse('show_best', kwargs = {'name_id':self.name})


class Janr(models.Model):
    name = models.CharField(max_length = 255, verbose_name = "Жанр игры")
    content = models.TextField(blank = True, verbose_name = "Описание жанра")
    photo = models.ImageField(upload_to = "photos/%Y/%m/%d/", verbose_name = "Фото")
    time_create = models.DateTimeField(auto_now_add = True, verbose_name = "Время создания")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанры игр'
        verbose_name_plural = 'Жанры игр'

    def get_absolute_url(self):
        return reverse('show_janr', kwargs = {'name_id':self.name})