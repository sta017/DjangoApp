
from django.urls import path
from . import views


urlpatterns = [
   path('',views.operation),
   path('submit/', views.handleSubmit, name='submit'),
]


