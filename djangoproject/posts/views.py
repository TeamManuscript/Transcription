# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author' : 'CoreyMS',
        'title' : 'Post 1',
        'content' : 'First post content',
        'date_posted' : 'July 3, 2019'
    },
    {
        'author' : 'Jane Doe',
        'title' : 'Post 2',
        'content' : 'second post content',
        'date_posted' : 'June 12, 2019'
    },

]

def index(request):
    context = {
        'posts' : posts
    }
    return render(request, 'posts/index.html', context)

def about(request):
    #return HttpResponse('about')
    return render(request, 'posts/about.html')
