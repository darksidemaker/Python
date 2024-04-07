import datetime
from django.shortcuts import render, redirect
from .utils import get_token, search_artist, get_song, client_id, client_secret,SPOTIFY_REDIRECT_URI,auth_url,token_url
from django.http import HttpResponse
from django.conf import settings
import requests
import  urllib.parse
from django.shortcuts import redirect, render
import requests

def index(request):
    return render(request, 'spotify_search/index.html')

def search(request):
    if request.method == 'POST':
        artist_name = request.POST.get('artist_name')
        token = get_token()
        result = search_artist(token, artist_name)
        if result:
            artis = result["artists"]["items"]
            track= result["tracks"]["items"]
            album= result["albums"]["items"]
            
            return render(request, 'spotify_search/index.html', {'artists': artis, 'tracks': track, 'albums':album})
        else:
            message = "No artist found with that name."
            return render(request, 'spotify_search/index.html', {'message': message})
    return render(request, 'spotify_search/index.html')

def login(request):
    # Redirect users to Spotify authorization page
    # clientid = client_id
    redirect_uri = SPOTIFY_REDIRECT_URI
    scope = 'user-read-private user-read-email'  # Adjust scope based on your requirements
    spotify_authorize_url = f'https://accounts.spotify.com/authorize?client_id={client_id}&response_type=code&redirect_uri={redirect_uri}&scope={scope}'
    return redirect(spotify_authorize_url)
# def login(request):
#     scope = 'user-read-private user-read-email'
#     prame={
#       'response_type': 'code',
#       'client_id': client_id,
#       'scope': scope,
#       'redirect_uri': SPOTIFY_REDIRECT_URI,
#       'show_dilog': True
#     }
#     auth_url_me = f"{auth_url}?{urllib.parse.urlencode(prame)}"
#     return redirect(auth_url_me)

# def callback(request):
#     print(request.GET)
#     if 'error' in request.GET:    
#         return render('profile/profile.html',{'error': request.args['error']})
    
#     if 'code' in request.GET:
    
#         authorization_code = request.GET.get('code') 
#         print("authorization_code "+authorization_code)
#         req_body={
#             'code' : request.GET['code'],
#             'grant_type':'authorization_code',
#             'client_id': client_id,
#             'client_secret': client_secret
#         }
        
#         response = requests.post(token_url, data= req_body)
#         token_info = response.json()
#         print(token_info)
        
#         request.session['access_token'] = token_info['access_token']
#         request.session['refresh_token']=token_info['refresh_token']
#         request.session['expires_at']= datetime.now().timestamp() + token_info['expires_in']
        
#         return render('profile/profile.html',{'info': request.session})
#         # return HttpResponseRedirect('/profile/')



def callback(request):
    if 'code' in request.GET:
        # Exchange authorization code for access token
        code = request.GET['code']
        # client_id = client_id
        # client_secret = client_secret
        redirect_uri = SPOTIFY_REDIRECT_URI
        token_url = 'https://accounts.spotify.com/api/token'
        data = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': redirect_uri,
            'client_id': client_id,
            'client_secret': client_secret
        }
        response = requests.post(token_url, data=data)
        token_info = response.json()
        access_token = token_info.get('access_token')
        if access_token:
            request.session['access_token'] = access_token
            # Redirect to profile or home page
            return redirect('profile')
    return render(request, 'login.html')


def profile(request):
    # Retrieve access token from session
    access_token = request.session.get('access_token')

    if access_token:
        # Make authorized request to Spotify API's user profile endpoint
        profile_url = 'https://api.spotify.com/v1/me'
        headers = {
            'Authorization': f'Bearer {access_token}'
        }
        response = requests.get(profile_url, headers=headers)
        print(access_token)
        if response.status_code == 200:
            # Parse JSON response
            profile_data = response.json()
            # Extract relevant profile details
            display_name = profile_data.get('display_name')
            email = profile_data.get('email')
            # Pass profile details to template for rendering
            return render(request, 'profile/profile.html', {'display_name': display_name, 'email': email})
        else:
            return render(request, 'profile/profile.html', {'error_message': 'Failed to fetch user profile'})
    else:
        return render(request, 'profile/profile.html', {'error_message': 'Access token not found in session'})