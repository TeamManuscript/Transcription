from django.urls import path
from.import views
from django.urls import re_path
from django.conf.urls import url
from django.contrib import admin

from django.urls import include, path
from accounts import views as accounts_views
from discussions import views as discussion_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from posts import views as posts_views
from django.contrib.auth import views as auth_views


app_name = 'discussions'

urlpatterns = [
    path('',views.discussion_board, name="board"),
    path('', views.discussion_board, name='board'),
    path('create/',views.discussion_create, name="create"),
    #this url must always precede the slug
    #url(r'^(?P<slug>[\w-]+)/$',views.discussion_detail),
    path('(<slug>[\w-]+)/', views.discussion_detail, name="detail"),
    #path('<int:slug>/', views.discussion_detail, name='detail'),
    path('admin/', admin.site.urls),
    # path('', include('posts.urls')),
    # path('posts/', include('posts.urls')),
    path('accounts/', include('accounts.urls')),
    # path('discussions/', include('discussions.urls')),
    path('about/',posts_views.about, name="about"),
     path('transcription/', include('males.urls')),
     path('homepage/', views.logout_view, name='logout'),
     path('collection/', views.collection, name = "collection"),

]
