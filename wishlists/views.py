from django.shortcuts import render

# Create your views here.


def wishlist(request):
    """ Display user's wishlist """
    template = 'wishlists/wishlist.html'
    context = {}

    return render(request, template, context)
