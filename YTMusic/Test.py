from ytmusicapi import YTMusic

ytmusic = YTMusic() 
# from ytmusicapi import YTMusic
# ytmusic = YTMusic("oauth.json")
# playlistId = ytmusic.create_playlist("test", "test description")

name= input("Enter song name:")
search_results = ytmusic.search(name)
# Print the numbers from 1 to 10
for i in range(0, 11):
	if search_results[i]['category'] == 'Songs':
  		print(search_results[i]['title'])
   		

vId=search_results[1]['videoId']
# vD= search_results[1]['duration_seconds']


# import requests

# url = "https://youtube-to-mp315.p.rapidapi.com/download"

# querystring = {"url":"https://www.youtube.com/watch?v="+vId,"endTime": vD,"format":"mp3"}

# payload = {}
# headers = {
# 	"content-type": "application/json",
# 	"X-RapidAPI-Key": "413274f3abmsh08272ab528a1e6dp1d00fdjsn6feda39036b4",
# 	"X-RapidAPI-Host": "youtube-to-mp315.p.rapidapi.com"
# }

# response = requests.post(url, json=payload, headers=headers, params=querystring)

# print(response.json())
# # ytmusic.add_playlist_items(playlistId, [search_results[1]['videoId']])

video_url="https://www.youtube.com/watch?v="+vId
output_path="/workspaces/Python/YTMusic/mp3file"
from pytube import YouTube

def download_audio(video_url, output_path):
    try:
        yt = YouTube(video_url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_stream.download(output_path)
        print("Audio downloaded successfully!")
    except Exception as e:
        print("Error:", e)


# download_audio(video_url, output_path)
