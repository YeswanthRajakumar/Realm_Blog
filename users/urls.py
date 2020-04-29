from django.urls import path, include
from users import views as users_views

urlpatterns = [

    path('login/', users_views.UserLogin, name='user-login'),
    path('logout/', users_views.UserLogout, name='user-logout'),
    path('register/', users_views.register, name='user-register'),
    path('profile/<int:user_id>', users_views.profile, name='user-profile'),
]
