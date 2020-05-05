from django.shortcuts import render, redirect, HttpResponseRedirect

from .models import *

def registration(request):
    print('taking request', request) #for debugging
    if request.method == 'POST':
        student_object = users.objects.create()
        student_object.firstname = request.POST['firstname']
        student_object.lastname = request.POST['lastname']
        student_object.email = request.POST['email']
        student_object.password = request.POST['password']
        student_object.birthday = request.POST['birthday']
        student_object.gender = request.POST['gender']
        print('firstname', request.POST['firstname'])
        print('lastname', request.POST['lastname'])
        print('email', request.POST['email'])
        print('password', request.POST['password'])
        print('birthday', request.POST['birthday'])
        print('gender', request.POST['gender'])
        student_object.save()
        if student_object:
            return render(request, 'registration.html', {'success':'successfully registered'})
        else:
            return render(request, 'registration.html', {'Error':'user exists, Try with different emailID'})

    return render(request, 'registration.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pwd']
        student_object = users.objects.filter(email=email, password=password)
        if student_object:
            return HttpResponseRedirect('/students/home')
        else:
            return render(request, 'login.html', {'error': 'email id and password did not match, Try again'})

    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def forgotPWD(request):
    if request.method == 'POST':
        email = request.POST['email']
        student_object = users.objects.filter(email=email)
        if student_object:
            return render(request, 'forgotPWD.html', {'success': 'Link has been sent to your email id'})
        else:
            return render(request, 'forgotPWD.html', {'error':'email ID does not exists, Try with different emailID'})

    return render(request, 'forgotPWD.html')


# Create your views here.
