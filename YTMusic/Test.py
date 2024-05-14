from ytmusicapi import YTMusic

ytmusic = YTMusic() 

name= input("Enter song name:")

search_results = ytmusic.search(name)

vId=search_results[1]['videoId']

video_url="https://www.youtube.com/watch?v="+vId
output_path="/workspaces/Python/YTMusic/mp3file"
print(video_url)
print(search_results[1])
from pytube import YouTube

def download_audio(video_url, output_path):
    try:
        yt = YouTube(video_url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_stream.download(output_path)
        print(audio_stream.download(output_path))
        print("Audio downloaded successfully!")
    except Exception as e:
        print("Error:", e)


# download_audio(video_url, output_path)

import pytube
import os

try:
 
 
    video = pytube.YouTube(video_url).streams.filter(only_audio=True).first().download(output_path)

    base, ext = os.path.splitext(video)

    new_file = base + '.mp3'
    os.rename(video, new_file)


    yt = pytube.YouTube(video_url)
    title = yt.title

    print(f"{title} has been successfully downloaded in .mp3 format.")
except Exception as e:
    print("Error:", e)