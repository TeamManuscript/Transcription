from django.conf.urls import url
from django.contrib import admin

from djangoproject import views
from django.urls import include, path
from accounts import views as accounts_views
from discussions import views as discussion_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    path('posts/', include('posts.urls')),
    path('accounts/', include('accounts.urls')),
    path('discussions/', include('discussions.urls')),
    path('transcription/', include('males.urls')),
    path('', discussion_views.discussion_board, name="home"),
    #url(r'^$',views.index),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    from django.conf.urls.static import static
    import debug_toolbar
    urlpatterns = [
        url('__debug__/', include(debug_toolbar.urls))
    ]+urlpatterns
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
