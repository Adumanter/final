from django.db import models


class Craft(models.Model):
    title = models.CharField(max_length=100, unique=True, null=False)
    content = models.TextField(max_length=2500, null=False)
    image = models.FileField(null=False, upload_to='upload/')
    published = models.DateTimeField(null=False, auto_now=True)

    def __str__(self):
        return self.title
