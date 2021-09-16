from django.db import models
from publications.models import Article


class Contact(models.Model):
    name = models.CharField(max_length=300, null=False, verbose_name='Имя')
    email = models.EmailField()
    telephone = models.CharField(max_length=100, null=True, verbose_name='Телефон')
    message = models.TextField(verbose_name='Сообщение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
