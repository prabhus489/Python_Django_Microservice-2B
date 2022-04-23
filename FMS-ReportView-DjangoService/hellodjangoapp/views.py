from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from hellodjangoapp.models import Student
from hellodjangoapp.models import Customer
from hellodjangoapp.models import Market

def homePageView(request):
    return HttpResponse('Welcome to Django Application!, Your are Currently viewing Django based application running on port 8000!')


def numbers_show(request):
    x = []
    for i in range(10):
        x.append(i)
    return HttpResponse("<h1>List of numbers</h1> The Digits are {0}".format(x))


def student_show(request):
    students = Student.objects.all()
    return render(request, "show.html",{'student':students})


def customer_show(request):
    customers = Customer.objects.all()
    return render(request, "show.html",{'customer':customers})


def market_show(request):
    markets = Market.objects.all()
    return render(request, "show.html",{'market':markets})

def report_show(request):
    students = Student.objects.all()
    customers = Customer.objects.all()
    markets = Market.objects.all()
    return render(request, "show.html",{'student':students,'customer':customers,'market':markets})










