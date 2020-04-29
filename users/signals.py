from django.contrib.auth.models import User
from django.db.models.signals import post_save
from blog.models import Author


def createAuthorProfileSignal(sender, instance, created, **kwargs):
    if created:
        Author.objects.create(user=instance)
        print('profile created for : ', instance)


post_save.connect(createAuthorProfileSignal, sender=User)
