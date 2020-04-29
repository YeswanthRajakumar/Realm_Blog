from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.

class Category(models.Model):
    category_tag = models.CharField(max_length=30)

    def __str__(self):
        return self.category_tag


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,)
    email = models.EmailField(null=True, blank=True)
    profile_pic = models.ImageField(null=True, default='default.jpg')
    contact = models.CharField(max_length=10, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    website_link = models.URLField(blank=True, null=True)
    interested_items = models.ManyToManyField(Category)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=100)
    content = RichTextField(blank=True, null=True)
    posted_date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(null=True)
    no_of_views = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
