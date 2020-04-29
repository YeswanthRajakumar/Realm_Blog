from django.urls import path

from blog import views as blog_views

urlpatterns = [
    path('', blog_views.home, name='home'),
    path('blog/', blog_views.blogList, name='blog-list'),
    path('search/', blog_views.blogSearch, name='blog-search'),
    path('add/', blog_views.CreatePost, name='create-post'),
    path('update/<int:post_id>', blog_views.UpdatePost, name='update-post'),
    path('delete/<int:post_id>', blog_views.DeletePost, name='delete-post'),
    path('blogdetail/<int:id>', blog_views.blogDetailView, name='blog-detail'),

]
