from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from .forms import ApplicationForm
from .models import Application


def home(request):
    """Render the home page."""
    return render(request, "home.html")


@require_http_methods(["GET", "POST"])
def apply(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save()
            messages.success(
                request,
                f"Thank you for your application! We'll review it and get back to you soon."
            )
            return redirect('apply_success', application_id=application.id)
        else:
            messages.error(request, "Please fix the errors below and try again.")
    else:
        form = ApplicationForm()

    context = {
        'form': form,
        'page_title': 'Apply for PyCon Uganda Diversity Program',
    }
    return render(request, 'diversity_applications/apply.html', context)


def apply_success(request, application_id=None):
    context = {
        'application_id': application_id,
        'page_title': 'Application Submitted Successfully',
    }
    return render(request, 'diversity_applications/apply_success.html', context)
