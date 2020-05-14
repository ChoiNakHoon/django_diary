from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.conf import settings
from .models import Post
from .form import postForm

all_posts = Post.objects.all()

def index(request):
    return render(request, "index.html", {'blogs': all_posts})

def detail(request, id):
    blog_detail = get_object_or_404(Post, pk=id)
    return render(request, "blog/detail.html" , {'blog': blog_detail})

def boardwrite(request):
    form = postForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            Post.objects.create(
                author = auth.get_user_model().objects.get(username='jeong_e'),
                title = form.cleaned_data['title'],
                descript = form.cleaned_data['descript']
            )
        return redirect('main')
    else:
        return render(request, "blog/boardwrite.html" , {'form': form})