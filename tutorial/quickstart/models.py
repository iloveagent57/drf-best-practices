from django.conf import settings
from django.db import models


class Publication(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        null=False,
        unique=True,
        max_length=1024,
    )

    def __str__(self):
        return f'<Publication: {self.name}>'


class Article(models.Model):
    publication = models.ForeignKey(
        Publication,
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        null=False,
        unique=True,
        max_length=1024,
    )

    def __str__(self):
        return f'<Article: {self.title}>'
