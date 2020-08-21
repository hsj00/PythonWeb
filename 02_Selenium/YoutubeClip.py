from pytube import YouTube
from pprint import pprint

yt = YouTube("https://www.youtube.com/watch?v=QTjZJzYWzEU")

# title = yt.title
# descr = yt.vid_descr

# for stream in yt.streams.all():
#     pprint(str(stream))

pprint(yt.streams.filter(res='1080p').order_by('resolution').all())
pprint(yt.streams.filter(type='audio').all())
yt.streams.filter(res='1080p').order_by('resolution').first().download()
# yt.streams.filter(type='audio').all().first().download()
# yt.streams.filter(only_audio=True).first().download()
# pprint(yt.streams.filter(progressive=False, file_extension='mp4').desc())
