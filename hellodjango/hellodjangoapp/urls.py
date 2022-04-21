from django.urls import path
from .views import homePageView
from .views import numbers_show
from .views import student_show



urlpatterns = [
    path('', homePageView, name='home'),
    path('list/', numbers_show, name ='numbers_show'),
    path('studentlist/', student_show, name ='student_show')
]
