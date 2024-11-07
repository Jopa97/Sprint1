# tests_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('take_test/<int:test_id>/', views.take_test, name='take_test'),
    path('profile/', views.profile, name='profile'),
]