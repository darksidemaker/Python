APIkey= '91ea77cc28017f1304389481d53dee16'
secret=	'f7c73c2770766e626f4dd39c7b0071dc'
import requests

def get_top_artists(user):
    url = f'http://ws.audioscrobbler.com/2.0/?method=user.gettopartists&user={user}&api_key={APIkey}&format=json'
    response = requests.get(url)
    data = response.json()
    return data

user = input("Enter Last.fm username: ")
top_artists = get_top_artists(user)
if 'topartists' in top_artists:
    print("Top Artists:")
    for artist in top_artists['topartists']['artist']:
        print(artist['name'])
else:
        print("No top artists found for this user.")
