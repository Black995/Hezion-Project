from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import *
 
def index (request):
    latest_posts = Post.objects.order_by('-pub_date')[:5]
    context = {
        'latest_posts': latest_posts,
    }
    return render(request, 'blogapp/index.html', context)

def create (request):
    return render(request, 'blogapp/create.html')

def createpost (request):
    post = Post(title=request.POST['title'], content=request.POST['content'], imageurl=request.POST['imageurl'])
    post.save()
    return HttpResponseRedirect(reverse('index'))

def detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'blogapp/detail.html', {'post': post})

def update(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'blogapp/updatepost.html', {'post': post})

def updatepost (request, post_id):
    post = Post.objects.get(pk=post_id)
    post.title = request.POST['title']
    post.content = request.POST['content']
    post.imageurl = request.POST['imageurl']
    post.save()
    return HttpResponseRedirect(reverse('index'))
