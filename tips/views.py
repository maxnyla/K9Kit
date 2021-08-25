from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Tip
from .forms import TipForm


def tips(request):
    """ A view showing all site tips """

    tips = Tip.objects.all()

    template = 'tips/tips.html'
    context = {
        'tips': tips,
    }

    return render(request, template, context)


def view_tips(request):
    """ A view displaying all tips available """
    
    tips = Tip.objects.all()

    template = 'tips/view_tips.html'
    context = {
        'view_tips' : view_tips,
    }

    return render(request, template, context)


@login_required
def add_tip(request):
    """ A view for logged in users to add a tip post """

    if request.method == 'POST':
        form = TipForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks! Your tip was added')

            return redirect(reverse('tips',))
        else:
            messages.error(request, 'Failed to add tip.\
                                    Please ensure form is valid and try again.')
    else:
        form = TipForm()

    form = TipForm()
    template = 'tips/add_tip.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_tip(request, tip_id):
    """ A view for logged in users to edit their tip """

    tip = get_object_or_404(Tip, pk=tip_id)
    if request.method == 'POST':
        form = TipForm(request.POST, instance=tip)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your tip was successfully edited.')

            return redirect(reverse('tips'))
        else:
            messages.error(request, 'Failed to edit tip. \
                    Please check the form is valid and try again.')
    else:
        form = TipForm(instance=tip)

    template = "tips/edit_tip.html"
    context = {
        "form": form,
        "tip": tipw,
    }

    return render(request, template, context)


@login_required
def delete_tip(request, tip_id):
    """ A view for logged in users to delete their tip """

    tip = get_object_or_404(Tip, pk=tip_id)
    tip.delete()
    messages.success(request, 'Your tip was deleted!')

    return redirect(reverse('tips'))
