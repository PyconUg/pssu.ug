from django.shortcuts import render, redirect

COUNTRIES = [
    ('rwanda', 'Rwanda'),
    ('kenya', 'Kenya'),
    ('tanzania', 'Tanzania'),
]

STATUS_CHOICES = [
    ('student', 'Student'),
    ('employed', 'Employed'),
    ('freelancer', 'Freelancer'),
    ('other', 'Other'),
]

PYTHON_LEVEL_CHOICES = [
    ('beginner', 'Beginner'),
    ('intermediate', 'Intermediate'),
    ('advanced', 'Advanced'),
]

PYTHON_DURATION_CHOICES = [
    ('lt_6m', '< 6 months'),
    ('6_12m', '6–12 months'),
    ('1_2y', '1–2 years'),
    ('2y_plus', '2+ years'),
]

INTEREST_CHOICES = [
    ('ai_ml', 'AI / Machine Learning'),
    ('web_dev', 'Web Development'),
    ('data_science', 'Data Science'),
    ('open_source', 'Open Source'),
    ('devops_cloud', 'DevOps / Cloud'),
]

SUPPORT_CHOICES = [
    ('travel', 'Travel'),
    ('accommodation', 'Accommodation'),
    ('conference_ticket', 'Conference Ticket'),
    ('none', 'None'),
]

FORM_CONTEXT = {
    'countries': COUNTRIES,
    'status_choices': STATUS_CHOICES,
    'python_level_choices': PYTHON_LEVEL_CHOICES,
    'python_duration_choices': PYTHON_DURATION_CHOICES,
    'interest_choices': INTEREST_CHOICES,
    'support_choices': SUPPORT_CHOICES,
}


def home(request):
    return render(request, "home.html")


def apply(request):
    if request.method == 'POST':
        return redirect('apply_success')
    return render(request, "apply.html", FORM_CONTEXT)


def apply_success(request):
    return render(request, "apply_success.html")
