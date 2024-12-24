from django.contrib import admin

from .models import Article, Picture, Article_joint_picture

admin.site.register(Article)
admin.site.register(Picture)
admin.site.register(Article_joint_picture)