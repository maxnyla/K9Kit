from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Newsletter
from .forms import NewsletterForm


def newsletters(request):
    """
    A view showing all newsletters
    """
    newsletters = Newsletter.objects.all()

    context = {
        'newsletters': newsletters,
    }

    return render(request, 'newsletters/newsletters.html', context)


@login_required
def add_newsletter(request):
    """
    A view for logged in site owners to add a newsletter
    """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only K9Kit admin has permission to do this.')
        return redirect(reverse('newsletter'))

    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks! Your newsletter was added')
            return redirect(reverse('newsletters',))
        else:
            messages.error(
                request, 'Failed to add newsletter.\
                        Please ensure form is valid and try again.')
    else:
        form = NewsletterForm()

    form = NewsletterForm()
    template = 'newsletters/add_newsletter.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_newsletter(request, newsletter_id):
    """
    A view for logged in site owners to edit their newsletter
    """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only K9Kit admin has permission to do this.')

        return redirect(reverse('newsletter'))

    newsletter = get_object_or_404(Newsletter, pk=newsletter_id)
    if request.method == 'POST':
        form = NewsletterForm(request.POST, instance=newsletter)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your newsletter was successfully edited.')

            return redirect(reverse('newsletters'))
        else:
            messages.error(request, 'Failed to edit newsletter. \
                    Please check the form is valid and try again.')
    else:
        form = NewsletterForm(instance=newsletter)

    template = "newsletters/edit_newsletter.html"
    context = {
        "form": form,
        "newsletter": newsletter,
    }

    return render(request, template, context)


@login_required
def delete_newsletter(request, newsletter_id):
    """
    A view for logged in site owners to delete their newsletter
    """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only K9Kit admin has permission to do this.')

        return redirect(reverse('newsletter'))
    newsletter = get_object_or_404(Newsletter, pk=newsletter_id)
    newsletter.delete()
    messages.success(request, 'Your newsletter was deleted!')

    return redirect(reverse('newsletters'))
