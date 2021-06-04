from django.urls import path
from . import views

app_name = "pages"

urlpatterns = [
    path('', views.index, name="index"),

    # page
    path('create/', views.create, name="create"),
    path('<int:pk>/', views.detail, name="detail"),
    path('<int:pk>/update/', views.update, name="update"),
    path('<int:pk>/delete/', views.delete, name="delete"),

    # comment crud
    path('<int:page_pk>/comments/create', views.create_comment, name="create"),
    path('<int:page_pk>/comments/<int:comment_id>/update', views.update, name="update"),
    path('<int:page_pk>/comments/<int:comment_id>/delete/', views.delete, name="delete"),
]