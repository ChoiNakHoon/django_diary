from django.shortcuts import render, get_object_or_404

from .models import Post

all_posts = Post.objects.all()

def index(request):
    return render(request, "index.html", {'blogs': all_posts})

def detail(request, id):
    blog_detail = get_object_or_404(Post, pk=id)
    return render(request, "blog/detail.html" , {'blog': blog_detail})