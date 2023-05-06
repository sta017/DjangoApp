from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.insurance_form, name='insurance_form'),
]
