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
@login_required
def add_post(request):
    """ Add a new blog post """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('blog'))

    form = PostForm(request.POST or None)
    template = 'add_post.html'

    try:
        if form.is_valid():
            form.save()
            messages.success(request,
                             f'Yahoo! A new blog post has been uploaded \
                             to the database')

            return redirect(reverse('blog', args=[post.id]))

    except Exception as e:
        form = PostForm()
        messages.warning(request,
                         'Blog post was not saved. Error: {}'.format(e))

    context = {
        'form': form,
    }

    return render(request, template, context)


# Edit a blog post on Blog page
# Help from Master Code Online
@login_required
def edit_post(request, pk):
    """ Edit an existing blog post """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('blog'))

    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'You have successfully edited this post!')
            return redirect(reverse('blog'))
        else:
            messages.error(request,
                           'Error: Blog post was not saved.')
    else:
        form = PostForm(instance=post)

    template = 'edit_post.html'
    context = {
        'form': form,
        'post': post,
        }

    return render(request, template, context)


# Delete a post from the blog page
@login_required
def delete_post(request, pk):
    """ Delete a post from the blog """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('blog'))

    post = get_object_or_404(Post, pk=pk)
    post.delete()
    messages.success(request, 'Post deleted!')
    return redirect(reverse('blog'))
