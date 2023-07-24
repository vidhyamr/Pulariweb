from django.urls import path
from . import views

app_name='collegeapp'

urlpatterns = [
    path('',views.home,name='home'),

]