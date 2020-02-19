from django.shortcuts import render, redirect
from.models import Discussion
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from.import forms

# Create your views here.
def discussion_board(request):
    discussions = Discussion.objects.all().order_by('date')
    return render(request, 'discussions/discussion_board.html',{'discussions': discussions})

def discussion_detail(request, slug):
    discussion = Discussion.objects.get(slug=slug)
    return render(request, 'discussions/discussion_detail.html', {'discussion': discussion})

def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('posts:index')

def collection(request):
    #return HttpResponse('about')
    return render(request, 'discussions/discussion_board.html')

@login_required(login_url="/accounts/login/")
def discussion_create(request):
    if request.method == 'POST':
        form = forms.CreateDiscussion(request.POST, request.FILES)
        if form.is_valid():
            #save discussion to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('discussions:board')
    else:
        form = forms.CreateDiscussion()
        return render(request, 'discussions/discussion_create.html', {'form':form})
