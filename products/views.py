from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .models import Product, Categories
from .forms import ProductForm

# Create your views here.


def all_products(request):
    """ A view to show individual product details page """

    products = Product.objects.all()
    query = None
    category = None

    if request.GET:
        if 'categories' in request.GET:
            category = request.GET['categories']
            products = products.filter(categories__name__in=category)
            category = Categories.objects.filter(name__in=category)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "Sorry we didn't quite get that, please try again!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'category': category,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show all products, including sorting and search queries """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


def add_product(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'You successfully added a product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(
                request,
                'Failed to add product. Please check if form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
