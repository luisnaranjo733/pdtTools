from urllib import urlencode

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from roomDoctor.models import Person

import state

@login_required
def index(request):
    params = {'SELECTION_OPEN': state.selectionStatus()}
    if params['SELECTION_OPEN']:
        params['liveIns'] = Person.getLiveIns()
        for person in params['liveIns']:
            if person == request.user and person.isSelecting():
                return redirect(select)
    return render(request, 'roomDoctor/selectionIndex.html', params)

# check permissions
def startSelection(request):
    state.startSelection()
    return redirect(index)
 
@login_required 
def stopSelection(request):
    state.stopSelection()
    return redirect(index)
    
@login_required
def select(request):
    if request.method == 'GET':
        raw = Person.objects.filter(isLiveInField=True, selectedField=False)
        people = []
        for person in raw:
            if person != request.user:
                people.append(person)
        params = {'roomMates': people}
        return render(request, 'roomDoctor/select.html', params)
    else:
        roomMates = request.POST.getlist('roomMates')
        return HttpResponse(roomMates)
