from django.contrib.auth import login
from django.shortcuts import get_object_or_404, redirect, render
from .models import Post, Tag, Me
from .forms import PostForm
from django.contrib.auth.decorators import login_required

from .utils import update_views
from .filter import PostFilter

def home(request):
    posts = Post.objects.filter(private=False)[::-1]
    tags = Tag.objects.all()[::-1]
    me = Me.objects.all()[0]
    num_posts = len(posts)
        
    if num_posts > 6:
        posts = posts[:6]
    else:
        pass
    
    context = {
        'posts': posts,
        'tags': tags,
        'me': me,
        'num_posts': num_posts
        }
    
    # update_views(request, post)
    update_views(request, me)
    return render(request, 'base/index.html', context)

def posts(request):
    posts = Post.objects.filter(private=False)
    tags = Tag.objects.all()[::-1]
    myFilter = PostFilter(request.GET, queryset=posts)
    posts = myFilter.qs[::-1]
        
    context = {
        'posts': posts,
        'tags' : tags,
        'filters': myFilter
        }
    return render(request, 'base/posts.html', context=context)

def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    posts = Post.objects.filter(private=False)[::-1]
    context = {
        'post': post,
        'posts': posts
    }
    return render(request, 'base/post.html', context=context)

def profile(request):
    return render(request, 'base/profile.html')

## CRUD VIEWS


@login_required(login_url="base:home")
def post_form(request):
    form = PostForm()

    context = {
        'form': form
    }

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('base:posts')

    return render(request, 'base/post_form.html', context)

@login_required(login_url="base:home")
def update_form(request, slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)

    context = {
        'form': form
    }

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return redirect('base:posts')

    return render(request, 'base/post_form.html', context)

@login_required(login_url="base:home")
def deletePost(request, slug):
    post = Post.objects.get(slug = slug)
    
    context = {
        'post': post
    }

    if request.method == 'POST':
        post.delete()
        return redirect('base:posts')

    return render(request, 'base/delete.html', context)
