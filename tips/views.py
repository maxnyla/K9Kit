from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Tip


def tips(request):
    """ A view showing all site tips """
    tips = Tip.objects.all()

    context = {
        'tips': tips,
    }

    return render(request, 'tips/tips.html', context)


def view_tips(request):
    """ A view displaying all tips available """
    
    tips = Tip.objects.all()

    template = 'tips/view_tips.html'
    context = {
        'view_tips' : view_tips,
    }

    return render(request, template, context)
