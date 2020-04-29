from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Author, Comment
from django.db.models import Q, Count
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from blog.forms import PostForm
from django.core.mail import send_mail


def get_category_count():
    queryset = Post.objects.values('category__category_tag').annotate(Count('category__category_tag'))
    return queryset


def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    else:
        return None


# Create your views here.
def home(request):
    #     if request.method == 'POST':
    #         send_mail(subject='Request from user',
    #                   message='This is message',
    #                   from_email='yeswanthjayanthi@gmail.com',
    #                   recipient_list=['yeswanth.17it@kct.ac.in'],
    #                   fail_silently=False)
    return render(request, template_name='blog/home.html')


def blogList(request):
    posts = Post.objects.all().order_by('-posted_date')
    latest_posts = Post.objects.order_by('-posted_date')[0:3]
    context = {
        'posts': posts
    }
    return render(request, template_name='blog/bloglist.html', context=context)


def blogSearch(request):
    searchresults = []
    post_list = Post.objects.all()
    search_query = request.GET.get('q')
    print("Query : ", search_query)

    if search_query != '':
        searchresults = post_list.filter(
            Q(title__icontains=search_query) | Q(content__icontains=search_query)
        ).distinct()
        context = {}
        if search_query != {}:
            context = {
                'search_results': searchresults,
            }
        else:
            context = {
                'search_results': 'No Results',

            }
        return render(request, template_name='blog/searchResults.html', context=context)
    else:
        return redirect('blog-list')


@login_required(login_url='user-login')
def blogDetailView(request, id):
    post_object = get_object_or_404(Post, id=id)
    comments = Comment.objects.filter(post=post_object)
    comments_count = comments.count()
    latest_posts = Post.objects.order_by('-posted_date')[0:3]
    category_count = get_category_count()
    commentform = CommentForm()
    print('current_user : ', request.user.author)
    print('author : ', post_object.author)

    if request.user.author == post_object.author:
        edit_allowed = True
        print('Allow')
    else:
        edit_allowed = False
        print('Not Allow ')

    context = {
        'post': post_object,
        'latest_posts': latest_posts,
        'category_count': category_count,
        'form': commentform,
        'comments': comments,
        'comments_count': comments_count,
        'edit_allowed': edit_allowed
    }
    if request.method == 'POST':
        commentform = CommentForm(data=request.POST)
        commentform.save(commit=False)
        commentform.instance.name = request.user
        commentform.instance.post = post_object
        commentform.save()
        return redirect('blog-list')

    return render(request, template_name='blog/blog_detail.html', context=context)


@login_required(login_url='user-login')
def CreatePost(request):
    form = PostForm()
    author = get_author(request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect('blog-list')
        else:
            print(form.errors)
    context = {
        'author': author,
        'current_user': request.user,
        'form': form,
    }
    return render(request, template_name='blog/create_post.html', context=context)


@login_required(login_url='user-login')
def UpdatePost(request, post_id):
    instance = get_object_or_404(Post, id=post_id)
    form = PostForm(instance=instance)
    if request.method == 'POST':
        print('post ----->')
        form = PostForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('blog-list')
    context = {
        'form': form,

    }
    return render(request, template_name='blog/update_post.html', context=context)


@login_required(login_url='user-login')
def DeletePost(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('blog-list')
