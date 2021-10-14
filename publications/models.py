from django.db import models
from django.urls import reverse


class Article(models.Model):
    place = models.CharField(max_length=100, unique=True, null=False, verbose_name='Место')
    content = models.TextField(max_length=2500, null=False, verbose_name='Содержание')
    image = models.FileField(null=False, upload_to='upload/')
    url = models.URLField(max_length=1000)
    published = models.DateTimeField(null=False, auto_now=True, verbose_name='Дата публикации')
    address = models.CharField(max_length=300, null=False, verbose_name='Адрес')

    def __str__(self):
        return self.place

    def get_absolute_url(self):
        return reverse('article', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'