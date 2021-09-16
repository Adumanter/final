from django.db import models


class Article(models.Model):
    place = models.CharField(max_length=100, unique=True, null=False)
    content = models.TextField(max_length=2500, null=False)
    image = models.FileField(null=False, upload_to='upload/')
    url = models.URLField(max_length=1000)
    published = models.DateTimeField(null=False, auto_now=True)
    address = models.CharField(max_length=300, null=False)

    def __str__(self):
        return self.place