from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from blog.models import Category
from django.forms import models
from blog.models import Author
from django.forms.widgets import CheckboxSelectMultiple


class UserRegister(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdationForm(models.ModelForm):
    class Meta:
        model = Author
        fields = ['contact', 'bio', 'website_link', 'interested_items', 'profile_pic', ]

    def __init__(self, *args, **kwargs):
        super(UserUpdationForm, self).__init__(*args, **kwargs)

        self.fields["interested_items"].widget = CheckboxSelectMultiple()
        self.fields["interested_items"].queryset = Category.objects.all()
