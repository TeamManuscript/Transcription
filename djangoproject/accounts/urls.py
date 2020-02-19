from django.urls import path
from . import views
from accounts import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('', views.signup, name='signup'),
    path('', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('signout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('signup/', views.signup, name='signup'),

    #path('signout/', auth_views.LoginView.as_view(template_name='accounts/signout.html'), name='signout'),
    #path('signout/', views.signout, name='signout'),
    #path('signup/', user_views.create_user, name = 'signup'),
]
