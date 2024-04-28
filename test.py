import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_REDIRECT_URI = 'https://refactored-winner-p459g9p7p7x2g7g-8000.app.github.dev/callback'
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
# Create a Spotify client
client = spotipy.Spotify(auth_manager=spotipy.oauth2.SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=SPOTIFY_REDIRECT_URI))

# Search for a track
track = client.search(q='The Beatles - Hey Jude')

# Play the track
client.start_playback(uris=[track['tracks']['items'][0]['uri']])