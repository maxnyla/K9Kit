from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There are no items in your bag")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51J5y9QBxi5CkUTcXf46ZnP5evHuHx1soka3bikcR88L6hw0spZyGq6qYDlarybCcPRME0qTTVKDxvUeRJsMtrNxc00x8oiBJau',
        'client_secret': 'test client secret',
    }

    return render (request, template, context)

