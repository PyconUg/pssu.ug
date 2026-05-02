from django.urls import path

from . import views

app_name = 'diversity_applications'

urlpatterns = [
    path('', views.apply, name='apply'),
    path('success/<uuid:application_id>/', views.apply_success, name='apply_success'),
]
