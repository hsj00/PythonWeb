from pytube import YouTube
from pprint import pprint

yt = YouTube("https://www.youtube.com/watch?v=QTjZJzYWzEU")

pprint(yt.title)
pprint(yt.vid_descr)

# pprint(title, decribe)

for stream in yt.streams.all():
    pprint(stream)
