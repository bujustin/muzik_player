from django.shortcuts import *

import threading
import datetime

from .player.vlcplayer import VlcPlayer
from .queue.queue import Queue
from .search.search import *

class Interface(object):
    def __init__(self):
        self.player = VlcPlayer()
        self.queue = Queue()

        self.currentSong = getBlank()
        self.searchResults = []

        self.userCount = 0
        self.users = {}

    """
    Get Requests
    """
    def getIndexContext(self):
        context = {
            "queue": self.queue.getQueue(),
            "currentsong": self.currentSong
        }
        return context

    def getSearchContext(self, query):
        self.searchResults = getSongs(query)
        context = {
            "searchresults": self.searchResults
        }
        return context

    def getPoll(self):
        context = {
            "queue": self.queue.getQueue(),
            "currentsong": self.currentSong,
        }

        infoHtml = str(render_to_response("musicinfo.html", context))
        queueHtml = str(render_to_response("queue.html", context))
        friendlistHtml = str(render_to_response("friendlist.html", self.getUserContext()))

        data = {
            "info": infoHtml, 
            "infourl": self.currentSong["url"],
            "queue": queueHtml, 
            "queuelength": len(self.queue.getQueue()), 
            "position": self.player.getPosition(), 
            "length": self.currentSong["length"],
            "friendlist": friendlistHtml,
            "isplaying": self.player.isPlaying()
        } 

        return data

    def getQueueContext(self):
        context = {
            "queue": self.queue.getQueue(),
        }
        return context

    """
    Queue
    """
    def addToQueueFromSearch(self, index):
        song = self.searchResults[int(index) - 1]
        self.queue.addToQueue(song)

    def deleteFromQueue(self, index):
        self.queue.removeFromQueue(int(index))

    """
    Player
    """
    def playerPlay(self):
        if self.player.isEmpty() and self.queue.hasNext(): #if player is playing for first time
            self.timer()
        else: #if player is resuming
            self.player.Play()

    def playerPause(self):
        self.player.Pause()

    def playerSkip(self):
        self.playNext()

    def playerPrev(self):
        self.playPrev()

    def playerSetPos(self, q):
        percentage = int(q) / 100.0
        self.player.setPosition(percentage)

    """
    Friend List
    """
    def addUser(self):
        self.userCount += 1
        self.users[self.userCount] = "Friend " + str(self.userCount)
        return self.userCount

    def removeUser(self, index):
        del self.users[int(index)]

    def getUserContext(self):
        context = {
            "users": self.users.values()
        }
        return context

    """
    Song Selection
    """
    def timer(self):
        if self.player.isEnded() or self.player.isEmpty():
            self.playNext()

        threading.Timer(2, self.timer).start()

    def playNext(self):
        if self.queue.hasNext():
            self.currentSong = self.queue.getNext()
            self.player.Open(self.currentSong)
            self.player.Play()
        elif self.player.isEmpty or self.player.isEmpty():
            self.currentSong = getBlank()
            self.player.Pause()

    def playPrev(self):
        if self.queue.hasPrev():
            self.currentSong = self.queue.getPrev()
            self.player.Open(self.currentSong)
            self.player.Play()
