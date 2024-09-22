from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as my_views

urlpatterns = [
    path('login/', my_views.user_login, name="login"),
    path('register/', my_views.register, name="register"),
    path('logout/', auth_views.LogoutView.as_view(template_name="accounts/logout.html"), name="logout"),
]
