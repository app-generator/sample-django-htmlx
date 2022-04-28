
from django.urls import path
from BackendApp import views

urlpatterns = [
    path('signup/', views.Signup.as_view(), name="signup"),
    path('', views.Index.as_view(), name="index"),
    path('login/', views.Login.as_view(), name="login"),
    path('logout/', views.LogOut.as_view(), name="logout"),
]
