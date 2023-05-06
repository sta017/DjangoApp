#from django.urls import re_path
#from . import views

#urlpatterns = [
#    re_path(r'^submit/$', views.submit, name='submit'),
#    re_path(r'^display/$', views.display, name='display'),
#]


from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit, name='submit'),       #'submit/' just means this url will lead to executing submit function in views.py
    path('display/', views.display, name='display'),
]
