from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Tip
#from .forms import NewsletterForm


def tips(request):
    """ A view showing all site tips """
    tips = Tip.objects.all()

    context = {
        'tips': tips,
    }

    return render(request, 'tips/tips.html', context)
