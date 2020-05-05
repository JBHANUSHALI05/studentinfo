from django.urls import path
from . import views

urlpatterns = [
    path('registration', views.registration),
    path('login', views.login),
    path('home', views.home),
    path('forgotPWD', views.forgotPWD)

]
