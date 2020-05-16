from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.conf import settings
from django.core.paginator import Paginator
from .models import Post
from .form import postForm

all_posts = Post.objects.all()


def index(request):
    return render(request, "index.html", {'blogs': all_posts})


def detail(request, id):
    post_detail = get_object_or_404(Post, pk=id)
    return render(request, "blog/detail.html", {'post': post_detail})


def boardview(request):
    posts = all_posts.order_by('-id')
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    context = {
        'posts': posts,
        'pages': paginator.get_page(page)
    }
    return render(request, 'blog/boardview.html', context)


def boardwrite(request):
    form = postForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            Post.objects.create(
                author=auth.get_user_model().objects.get(username='jeong_e'),
                title=form.cleaned_data['title'],
                descript=form.cleaned_data['descript']
            )
        return redirect('boardview')
    else:
        return render(request, "blog/boardwrite.html", {'form': form})

def boardupdate(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = postForm(request.POST, instance = post)
        form.save()
        return render(request, 'blog/detail.html', {'post': post})
    
    form = postForm(instance = post)
    context = {
        'form' : form,
        'post' : post
    }
    return render(request, 'blog/boardupdate.html', context)

def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('boardview')