from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('signup/', views.signup, name="signup"), # Create
    path('myaccount/', views.myaccount, name="myaccount"), # Read, Update
    path('signout/', views.signout, name="signout"), # Delete
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),   
]