from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(
            request, "Whoops looks like there's nothing in your bag")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IdHYyKgGZvjBwcCY1mAOrWAV5lnDyAZI7y6UZ7Do5OKsjGwl6MsZFhLicwON2vshjiiy3frAybqNaIhMjXBJI2i00spF84cJv',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
