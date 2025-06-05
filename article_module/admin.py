from django.contrib import admin
from django.http import HttpRequest

from article_module import models
from article_module.models import Article, ArticleComment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'url_title', 'is_active', 'parent']
    list_editable = ['url_title', 'is_active', 'parent']

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_active', 'author']
    list_editable = ['is_active']

    def save_model(self, request:HttpRequest, obj: Article, form, change):
        if not change:
            obj.author = request.user
        return super().save_model(request, obj, form, change)

class ArticleCommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'create_date', 'parent']

admin.site.register(models.ArticleCategory, ArticleAdmin)
admin.site.register(models.Article, ArticlesAdmin)
admin.site.register(models.ArticleComment, ArticleCommentAdmin)