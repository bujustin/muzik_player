import threading
import datetime

#from .player.vlcplayer import VlcPlayer
from .queue.queue import Queue
from .search.search import *

class Interface(object):
    def __init__(self):
        #self.player = VlcPlayer()
        self.queue = Queue()

        self.currentSong = getBlank()
        self.searchResults = []

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

    def getSidebarContext(self):
        context = {
            "queue": self.queue.getQueue(),
            "currentsong": self.currentSong,
            "position": 0 #self.player.getPosition()
        }
        return context

    """
    Queue
    """
    def addToQueueFromSearch(self, index):
        song = self.searchResults[int(index) - 1]
        self.queue.addToQueue(song)

    def deleteFromQueue(self, index):
        self.queue.removeFromQueue(int(index) - 1)

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


    def timer(self):
        if self.player.isEnded() or self.player.isEmpty():
            self.playNext()

        threading.Timer(2, self.timer).start()

    def playNext(self):
        if self.queue.hasNext():
            self.currentSong = self.queue.getNext()
            self.player.Open(self.currentSong)
            self.player.Play()
        else:
            self.currentSong = getBlank()

    def playPrev(self):
        if self.queue.hasPrev():
            self.currentSong = self.queue.getPrev()
            self.player.Open(self.currentSong)
            self.player.Play()
