from django.urls import path
from . import views

urlpatterns = [
    # index
    path('', views.index),

    # create
    path('create/', views.create),
    path('create_proc/', views.create_proc),

    # read
    path('<int:pk>/', views.detail),

    # update
    path('<int:pk>/update/', views.update),
    path('<int:pk>/update_proc/', views.update_proc),

    # delete
    path('<int:pk>/delete/', views.delete),
]