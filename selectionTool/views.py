from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect

def home(request):
    return HttpResponse('/op')
