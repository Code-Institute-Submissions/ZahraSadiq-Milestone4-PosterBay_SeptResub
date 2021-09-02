from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, get_object_or_404
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
# Help from Master Code Online
def add_post(request):
    """ Add a new blog post """
    form = PostForm(request.POST or None)
    template = 'add_post.html'
    
    try:
        if form.is_valid():
            form.save()
            messages.success(request,
            f'Yahoo! A new blog post has been uploaded to the database')

            return redirect(reverse('blog'))

    except Exception as e:
        form = PostForm()
        messages.warning(request, 'Blog post was not saved. Error: {}'.format(e))

    context = {
        'form': form,
    }

    return render(request, template, context)
