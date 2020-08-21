from pytube import YouTube
import requests
import subprocess
import os
import ffmpeg

workdir = os.path.dirname(os.path.realpath(__file__))
url = input('playlist url : ').rstrip()

if 'watch' in url:
    url = 'https://youtube.com/playlist?list=' + \
        url.split('list=')[-1].split('&')[0]

res = requests.get(url)
source = res.text  # Response의 바디를 source라는 변수에 저장합니다. 이는 Raw Text 입니다.
vid_ids = [x.split('href="/watch?v=')[1].split('&amp;')[0]
           for x in source.split('\n') if 'pl-video-title-link' in x]


for vid in vid_ids:
    getStr = 'https://www.youtube.com/watch?v=' + vid
    yt = YouTube(getStr)
    file_name = yt.title
    print('Downloading %s' % (file_name))

    yt.streams.filter(adaptive=True, file_extension='mp4', only_video=True).order_by(
        'resolution').desc().first().download('./', 'video')
    yt.streams.filter(adaptive=True, file_extension='mp4', only_audio=True).order_by(
        'abr').desc().first().download('./', 'audio')
    output = ''

    result = subprocess.Popen(['ffmpeg', '-y', '-i', workdir + '/video.mp4', '-i', workdir + '/audio.mp4',
                               workdir + '/' + file_name.replace('/', '-') + '.mp4'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # Filename에 replace가 들어가는 이유는 "/" 문자가 들어갈 경우 파일이름이 아니라 디렉토리로 인식하기 떄문입니다. replace없이 바로 집어넣을 경우 문제가 발생합니다.
    out, err = result.communicate()
    exitcode = result.returncode
    if exitcode != 0:
        print(exitcode, out.decode('utf8'), err.decode('utf8'))
    else:
        print('Completed')
