from django.contrib import admin
from .models import Article, Publication, PublicationMembership, Tag

# Register your models here.
admin.site.register(Article)
admin.site.register(Publication)
admin.site.register(PublicationMembership)
admin.site.register(Tag)
