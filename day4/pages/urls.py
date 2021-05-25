from django.urls import path
from . import views

urlpatterns = [
    path('throw/', views.throw),
    path('catch/', views.catch),
]