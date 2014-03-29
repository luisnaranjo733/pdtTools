from urllib import urlencode
from email.utils import parseaddr

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.forms import EmailField
from django.core.exceptions import ValidationError

from roomDoctor.models import Person
    
def logIn(request):
    params = {}
    if request.method == 'POST':
        redirectUrl = request.GET.get('next') or '/'
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)

                return HttpResponseRedirect(redirectUrl) # Redirect after POST
            else:
                return HttpReponse("Your account has been disabled!")
        else:
            return HttpResponse("Your username and password were wrong!")
    return render(request, 'logIn.html', params)
        
def logOut(request):
    logout(request)
    return redirect('/')
    
def addUser(request):
    if request.method == 'GET':
        return render(request, 'addUser.html')
    else:
        return signUp(request)  
    
def signUp(request):
    email = request.POST.get('email')
    name = request.POST.get('name')
    password = request.POST.get('password')
    if not email or not name or not password or not isEmailValid(email):
        return HttpResponse("Make sure you include all of the fields, and a valid email address!")
    user = Person.objects.create_user(email, password=password)
    user.setName(name)
    user.save()
    return logIn(request)
    
def isEmailValid( email ):
    try:
        EmailField().clean(email)
        return True
    except ValidationError:
        return False