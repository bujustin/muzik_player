import vlc

class VlcPlayer(object):
    def __init__(self):
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.song = None
        self.length = 0

    def Open(self, song):
    	self.song = song
        self.length = song["length"]
    	self.media = self.instance.media_new(song["url"])
        self.player.set_media(self.media)
        
    def Play(self):
        self.player.play()

    def Pause(self):
    	self.player.pause()

    def getPosition(self): #Returns player position as a percentage of 1
        try:
            if self.player.get_state() == vlc.State.Ended or self.player.get_state() == vlc.State.NothingSpecial:
                return 0
            else:
                return self.player.get_position()
        except:
            return 0

    def isEmpty(self): #Return true if there is no media loaded
        if self.player.get_state() == vlc.State.NothingSpecial:
            return True
        else:
            return False

    def isEnded(self): #Return true if player finished playing loaded media
        if self.player.get_state() == vlc.State.Ended:
            return True
        else:
            return False

    def isPlaying(self):
        if self.player.get_state() == vlc.State.Ended or self.player.get_state() == vlc.State.NothingSpecial or self.player.get_state() == vlc.State.Paused:
            return False
        else:
            return True

    def setPosition(self, percentage):
        if percentage >= 0 and percentage < 1:
            self.player.set_position(percentage)
