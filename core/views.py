from urllib import urlencode

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
    
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