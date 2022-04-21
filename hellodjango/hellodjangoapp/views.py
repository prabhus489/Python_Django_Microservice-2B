from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from hellodjangoapp.models import Student

def homePageView(request):
    return HttpResponse('Hello, Django!')


def numbers_show(request):
    x = []
    for i in range(10):
        x.append(i)
    return HttpResponse("<h1>List of numbers</h1> The Digits are {0}".format(x))


def student_show(request):
    students = Student.objects.all()
    return render(request, "show.html",{'student':students})









