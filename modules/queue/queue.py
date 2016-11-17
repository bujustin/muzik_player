import pafy

class Queue(object):
    def __init__(self):
        self.queue = []
        self.history = []

    #adds a song to the end of the queue
    def addToQueue(self, song):
        try:
            video = pafy.new(song["url"])
            url = video.getbestaudio().url

            newSong = song
            newSong["url"] = "http://www.stephaniequinn.com/Music/Commercial%20DEMO%20-%2001.mp3" #url
            newSong["length"] = video.length
            self.queue.append(newSong)
        except:
            pass

    #remove the song object at the specified index from the queue
    def removeFromQueue(self, index):
        del self.queue[index]

    #return the song object at the specified index from the queue
    def getSongFromQueue(self, index):
        return self.queue[index]

    def getNext(self): 
        currentSong = self.queue.pop(0)
        self.history.append(currentSong)
        return currentSong

    def getPrev(self):
        self.queue.insert(0, self.history[len(self.history) - 1])
        del self.history[len(self.history) - 1]
        currentSong = self.history[len(self.history) - 1]
        return currentSong

    def getQueue(self):
        return self.queue

    def getHistory(self):
        return self.history

    def hasNext(self):
        return len(self.queue) > 0

    def hasPrev(self):
        return len(self.history) > 1