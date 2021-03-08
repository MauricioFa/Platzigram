"""Post Views"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
import random

# Forms
from posts.forms import PostForm

# Models
from posts.models import Post

class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all published posts"""
    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created')
    paginate_by = 255
    context_object_name = 'posts'

class PostDetailView(LoginRequiredMixin, ListView):
    """Return post details"""

    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'

@login_required
def create_post(request):
    """Create new post"""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:feed')
    else:
        form = PostForm()

    return render(
        request=request,
        template_name='posts/new.html',
        context={
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        }
        
    )