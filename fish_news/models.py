from django.db import models


class New(models.Model):
    title = models.CharField(max_length=100, unique=True, null=False, verbose_name='Заголовок')
    content = models.TextField(max_length=2500, null=False, verbose_name='Содержание')
    image = models.FileField(null=False, upload_to='upload/')
    published = models.DateTimeField(null=False, auto_now=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость о рыбалке'
        verbose_name_plural = 'Новости о рыбалке'

