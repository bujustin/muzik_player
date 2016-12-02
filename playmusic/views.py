from django.shortcuts import *
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

import simplejson
import sys
sys.path.append("..")
from modules.interface import Interface
interface = Interface()

def index(request):
    context = interface.getIndexContext()
    return render(request, "index.html", context)

def search(request, q):
    context = interface.getSearchContext(q)
    return render_to_response("search.html", context)

def poll(request):
    data = interface.getPoll()
    return HttpResponse(simplejson.dumps(data))

def add(request, q):
    interface.addToQueueFromSearch(q)
    context = interface.getQueueContext()
    return render_to_response("queue.html", context)

def delete(request, q):
    interface.deleteFromQueue(q)
    context = interface.getQueueContext()
    return render_to_response("queue.html", context)

def play(request):
    interface.playerPlay()
    return HttpResponseRedirect(reverse("index"))

def pause(request):
    interface.playerPause()
    return HttpResponseRedirect(reverse("index"))

def skip(request):
    interface.playerSkip()
    return HttpResponseRedirect(reverse("index"))

def prev(request):
    interface.playerPrev()
    return HttpResponseRedirect(reverse("index"))

def setpos(request, q):
    interface.playerSetPos(q)
    return HttpResponseRedirect(reverse("index"))
