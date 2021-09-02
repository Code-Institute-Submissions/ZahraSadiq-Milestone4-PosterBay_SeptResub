from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import Post 
from .forms import PostForm


# Create your views here.


# From build a blog app with django tutorial
# only published blog posts will appear on website
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


# Add a new blog post to Blog page
def add_post(request):
    """ Add a new blog post """
    form = PostForm(request.POST or None)
    template = 'add_post.html'
    
    if form.is_valid():
        form.save()

    else:
        form = PostForm()

    context = {
        'form': form,
    }

    return render(request, template, context)
