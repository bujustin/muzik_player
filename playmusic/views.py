from django.shortcuts import *
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from interface import *
interface = Interface()

def index(request):
    context = interface.getIndexContext()
    return render(request, "index.html", context)

def search(request, q):
    context = interface.getSearchContext(q)
    return render_to_response("search.html", context)

def poll(request):
    context = interface.getSidebarContext()
    return render_to_response("sidebar.html", context)

def add(request, q):
    interface.addToQueueFromSearch(q)
    return HttpResponseRedirect(reverse("index"))

def delete(request, q):
    interface.deleteFromQueue(q)
    return HttpResponseRedirect(reverse("index"))

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

