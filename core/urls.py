from django.contrib import admin
from django.urls import path, include
from website import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("apply/", views.apply, name="apply"),
    path("apply/success/", views.apply_success, name="apply_success"),
    path("events/", include("events.urls", namespace="events")),
]
