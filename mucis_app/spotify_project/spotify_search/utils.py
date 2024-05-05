import os
import base64
from requests import post, get
import json
import spotipy
from ytmusicapi import YTMusic

ytmusic = YTMusic()
# SPOTIFY_REDIRECT_URI = 'http://localhost:8000/callback'

auth_url='https://accounts.spotify.com/authorize'
token_url='https://accounts.spotify.com/api/token'
api_base='https://api.spotify.com/v1/'


SPOTIFY_REDIRECT_URI = 'https://refactored-winner-p459g9p7p7x2g7g-8000.app.github.dev/callback'
# redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")
redirect_uri = SPOTIFY_REDIRECT_URI
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
# oauth2 = spotipy.oauth2.SpotifyOAuth(client_id, client_secret)
oauth2 = spotipy.Spotify(auth_manager=spotipy.oauth2.SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri))
client = spotipy.Spotify(oauth2)

# Search for a track
track = client.search(q='The Beatles - Hey Jude')

# Play the track
client.start_playback(uris=[track['tracks']['items'][0]['uri']])

# auth_url='https://accounts.spotify.com/authorize'

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
    
    url = " https://accounts.spotify.com/api/token"
    headers={
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result =  json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return{"Authorization": "Bearer " + token}

def search_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"q={artist_name}&type=track%2Cartist%2Calbum&limit=10"
    
    # url= "https://api.spotify.com/v1/search" ?q={artist_name}&type=artist
    
    query_url = url +"?"+ query
    result = get(query_url, headers=headers)
    json_result =  json.loads(result.content)
    if len(json_result)==0:
        print("No artist with this name......")
        return None
    
    return json_result

def get_song(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result =  json.loads(result.content)["tracks"]
    return json_result

# def user_top(token):
#     url = f"https://api.spotify.com/v1/me/top/tracks?limit=10"
#     headers = get_auth_header(token)
#     result = get(url, headers=headers)
#     json_result =  json.loads(result.content)
#     return json_result


def ytmusic(name):
    