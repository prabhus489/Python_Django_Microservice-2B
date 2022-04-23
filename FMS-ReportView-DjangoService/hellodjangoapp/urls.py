from django.urls import path
from .views import homePageView
from .views import numbers_show
from .views import student_show
from .views import customer_show
from .views import market_show
from .views import report_show



urlpatterns = [
    path('', homePageView, name='home'),
    path('list/', numbers_show, name ='numbers_show'),
    path('studentlist/', student_show, name ='student_show'),
    path('customerlist/', customer_show, name ='customer_show'),
    path('marketlist/', market_show, name ='market_show'),
    path('reportlist/', report_show, name ='report_show')
]
