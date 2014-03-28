from urllib import urlencode

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

import state

@login_required
def index(request):
    params = {'SELECTION_OPEN': state.selectionStatus()}
    return render(request, 'selectionIndex.html', params)

@login_required
def startSelection(request):
    state.startSelection()
    return redirect(index)
    
def stopSelection(request):
    state.stopSelection()
    return redirect(index)