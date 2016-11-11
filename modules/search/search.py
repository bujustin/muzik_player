import json
import urllib2

ytkey = "AIzaSyDRNhlYHDjCTo_5AnAuYHbSb53YbnmQIRs"

def getSongs(q):
    getVideoList = urllib2.urlopen("https://www.googleapis.com/youtube/v3/search?q=" + q + "&key=" + ytkey + "&part=snippet&maxResults=20").read()
    jsonVideoList = json.loads(getVideoList)

    songs = []

    count = 0
    for i in xrange(len(jsonVideoList["items"])):
        if count >= 15:
            break
        if jsonVideoList["items"][i]["id"]["kind"] == "youtube#video":
            try:
                videoID = jsonVideoList["items"][i]["id"]["videoId"]
                url = "https://www.youtube.com/watch?v=" + videoID

                song = {
                "title": jsonVideoList["items"][i]["snippet"]["title"],
                "author": jsonVideoList["items"][i]["snippet"]["channelTitle"],
                "thumbnail": jsonVideoList["items"][i]["snippet"]["thumbnails"]["high"]["url"],
                "url": url,
                "length": 0
                }
                songs.append(song)
                count += 1
            except Exception:
                pass
    return songs

def getBlank():
    song = {
    "title": "",
    "author": "",
    "thumbnail": "https://pbs.twimg.com/profile_images/458794430200152064/XdQULww6_400x400.png",
    "url": "",
    "length": 0
    }
    return song
