from django.urls import path
from . import views

app_name='loginapp'

urlpatterns = [
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('student',views.student,name='student'),
    path('form',views.form,name='form'),
    path('about', views.about, name='about'),
    path('logout',views.logout,name='logout'),

]



