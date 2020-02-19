from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.main_home, name='main_page'),
    path('response/', views.response, name='text_response'),
    path('save', views.save,  name='save'),
]
