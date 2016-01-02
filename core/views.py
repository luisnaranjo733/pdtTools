from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def index(request):
    context = {}
    return render(request, 'index.html', context)