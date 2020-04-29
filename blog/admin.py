from django.contrib import admin
from .models import Author, Category, Post, Comment

# Register your models here.
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']


def approve_comments(request, queryset):
    queryset.update(active=True)
