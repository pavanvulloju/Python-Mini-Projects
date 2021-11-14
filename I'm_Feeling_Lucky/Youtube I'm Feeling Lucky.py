import urllib.request
import re

def getvideoURL(search_keyword):
	html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword.replace(' ','+'))
	video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
	videoID = video_ids[0]
	return 'https://www.youtube.com/watch?v='+videoID

videoURL = getvideoURL(input('Enter YouTube query: '))
print(videoURL)

