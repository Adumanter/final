from django.db import models
from django.urls import reverse


class Turnir(models.Model):
    title = models.CharField(max_length=150, null=False, verbose_name='Заголовок')
    published = models.DateTimeField(auto_now=True, verbose_name='Дата публикации')
    date = models.CharField(max_length=100, verbose_name='Дата события')
    place = models.CharField(max_length=300, verbose_name='Место проведения')
    phone = models.IntegerField(verbose_name='Телефон')
    image = models.FileField(upload_to='upload/')
    content = models.TextField(max_length=3000, verbose_name='Содержание')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('get_turnir', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
