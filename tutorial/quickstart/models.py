from django.conf import settings
from django.db import models


class Publication(models.Model):
    name = models.CharField(
        null=False,
        unique=True,
        max_length=1024,
        help_text='The name of the publication.',
    )

    def __str__(self):
        return f'<Publication: {self.name}>'


class PublicationMembership(models.Model):
    ADMIN = 'admin'
    USER = 'user'

    publication = models.ForeignKey(
        Publication,
        related_name='members',
        on_delete=models.CASCADE,
        help_text='The publication to which the member belongs.',
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='membership',
        on_delete=models.CASCADE,
        help_text='The User record associated with this membership.',
    )
    role = models.CharField(
        null=False,
        max_length=512,
        choices=[(ADMIN, 'Admin'), (USER, 'User')],
        help_text="The user's role as a member of the publication.",
    )

    def __str__(self):
        return f'<PubMembership: pub={self.publication.name}, user={self.user.username}, role={self.role}>'


class Article(models.Model):
    publication = models.ForeignKey(
        Publication,
        related_name='articles',
        on_delete=models.CASCADE,
        help_text='The publication in which this Article is published.',
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='articles',
        on_delete=models.CASCADE,
        help_text='The User who authored the Article.',
    )
    title = models.CharField(
        null=False,
        unique=True,
        max_length=1024,
        help_text='The title of the Article.',
    )

    def __str__(self):
        return f'<Article: title={self.title} author={self.author.username} pub={self.publication.name}>'
