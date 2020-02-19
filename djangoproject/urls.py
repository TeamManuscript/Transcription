from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from posts import views
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name = 'posts-index'),
    path('homepage/', auth_views.LogoutView.as_view(template_name='posts/index.html'), name='logout'),
    path('about/', views.about, name = 'posts-about'),
    #path('accounts/', accounts_views.signup, name='signup'),
    #url(r'^about/$', views.about),
    #url(r'^$',views.index),
]
