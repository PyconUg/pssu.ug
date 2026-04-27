from django.contrib import admin
from django.urls import path
from website import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("apply/<str:country>/", views.apply, name="apply"),
    path("apply/<str:country>/success/", views.apply_success, name="apply_success"),
]
