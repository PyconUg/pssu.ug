from django.urls import path
from . import views

app_name = "events"

urlpatterns = [
    path("", views.events_index, name="index"),
    path("django-girls/", views.django_girls, name="django_girls"),
    path("pyladies/", views.pyladies, name="pyladies"),
    path("persons-of-concern/", views.persons_of_concern, name="persons_of_concern"),
]
