from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


class Index(View):
    def get(self, request):
        return render(request, 'index.html', locals())


class Signup(View):        
    def get(self, request):
        return render(request, 'signup.html', locals())

    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("registerRepeatpassword")

        if password != confirm_password:
            return redirect('/signup/')
        
        exists = User.objects.filter(username=email).exists()
        if exists:
            return redirect('/signup/')
        else:
            User.objects.create_user(
                first_name=name,
                username=email,
                email=email,
                password=password,
                is_active=True
            )          
            return redirect('/login/')


class Login(View):
    def get(self, request):
        return render(request, 'login.html', locals())

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        exists = User.objects.filter(username=username).exists()
        if not exists:
            return redirect('/login/')
        else:
            user = User.objects.get(username=username)
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('/')
            else:
                return redirect('/login/')


class LogOut(View):
    def get(self, request):
        logout(request)
        return redirect('/login/')
