from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def home_page(request):
    return render(request, 'home_template/home_template.html')


def log_in_page(request):
    return render(request, 'login_signup_template/login.html')


def sign_up_page(request):
    return render(request, 'login_signup_template/signup.html')