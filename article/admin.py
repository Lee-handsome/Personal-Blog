from django.contrib import admin

from article.models import Article,Image

# Register your models here.
admin.site.register(Article)
admin.site.register(Image)