from django.shortcuts import render


def events_index(request):
    """Landing page listing all co-events."""
    co_events = [
        {
            "name": "Django Girls Workshop",
            "slug": "django-girls",
            "description": (
                "A free one-day workshop for women who want to learn how to build "
                "websites using Python and Django."
            ),
            "url_name": "events:django_girls",
        },
        {
            "name": "PyLadiesCon Africa",
            "slug": "pyladies",
            "description": (
                "A dedicated program within PyCon Africa 2026 designed to empower "
                "and support women in the Python ecosystem across the continent."
            ),
            "url_name": "events:pyladies",
        },
        {
            "name": "PyLadies Arua Refugee Python Workshop",
            "slug": "persons-of-concern",
            "description": (
                "A full-day, hands-on session introducing refugees and underserved "
                "youth to Python and web development, organised by PyLadies Kampala."
            ),
            "url_name": "events:persons_of_concern",
        },
    ]
    return render(request, "events/index.html", {"co_events": co_events})


def django_girls(request):
    return render(request, "events/django_girls.html")


def pyladies(request):
    context = {
        "title": "PyLadiesCon Africa",
        "description": (
            "PyLadiesCon Africa is a dedicated program within PyCon Africa 2026 "
            "designed to empower and support women in the Python ecosystem across "
            "the continent."
        ),
    }
    return render(request, "events/pyladies.html", context)


def persons_of_concern(request):
    context = {
        "title": "PyLadies Arua Refugee Python Web Development Workshop",
        "description": (
            "A full-day, hands-on session introducing refugees and underserved "
            "youth to Python and web development."
        ),
    }
    return render(request, "events/persons_of_concern.html", context)
