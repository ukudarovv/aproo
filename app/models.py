from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model


User = get_user_model()


class Author(models.Model):
    firstname = models.CharField(max_length=250, verbose_name='Имя', null=True)
    lastname = models.CharField(max_length=250, verbose_name='Фамилия', null=True)
    biography = models.TextField(verbose_name='Биография', null=True, blank=True)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.firstname


class Book(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название', null=True)
    author = models.ForeignKey('Author', verbose_name='Автор', on_delete=models.SET_NULL, null=True)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    publish_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', blank=True, null=True)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title


class Review(models.Model):
    content = models.TextField(verbose_name='Текст')
    rating = models.PositiveIntegerField(verbose_name='Оценка', default=0)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.SET_NULL, null=True, blank=True)
    book = models.ForeignKey(Book, related_name='reviews', verbose_name='Книга', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'

    def __str__(self):
        return self.user.username
