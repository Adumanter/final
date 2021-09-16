from django.db import models


class Turnir(models.Model):
    title = models.CharField(max_length=150, null=False)
    published = models.DateTimeField(auto_now=True)
    date = models.CharField(max_length=100)
    place = models.CharField(max_length=300)
    phone = models.IntegerField()
    image = models.FileField(upload_to='upload/')
    content = models.TextField(max_length=3000)

    def __str__(self):
        return self.title