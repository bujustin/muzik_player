import json
import urllib2
import re
ytkey = "AIzaSyDRNhlYHDjCTo_5AnAuYHbSb53YbnmQIRs"

def YTDurationToSeconds(duration):
  match = re.match('PT(\d+H)?(\d+M)?(\d+S)?', duration).groups()
  hours = _js_parseInt(match[0]) if match[0] else 0
  minutes = _js_parseInt(match[1]) if match[1] else 0
  seconds = _js_parseInt(match[2]) if match[2] else 0
  return hours * 3600 + minutes * 60 + seconds

def _js_parseInt(string):
    return int(''.join([x for x in string if x.isdigit()]))

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
                getVideo = urllib2.urlopen("https://www.googleapis.com/youtube/v3/videos?id=" + videoID + "&key=" + ytkey + "&part=contentDetails").read()
                jsonVideo =json.loads(getVideo)
                url = "https://www.youtube.com/watch?v=" + videoID
                song = {
                "title": jsonVideoList["items"][i]["snippet"]["title"],
                "author": jsonVideoList["items"][i]["snippet"]["channelTitle"],
                "thumbnail": jsonVideoList["items"][i]["snippet"]["thumbnails"]["high"]["url"],
                "url": url,
                "length": YTDurationToSeconds(jsonVideo["items"][0]["contentDetails"]["duration"])
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

