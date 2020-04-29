from blog.models import Post, Category,Comment
from django.forms import ModelForm
from django.forms.widgets import CheckboxSelectMultiple


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('category', 'title', 'content', 'thumbnail')

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        self.fields["category"].widget = CheckboxSelectMultiple()
        self.fields["category"].queryset = Category.objects.all()


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
