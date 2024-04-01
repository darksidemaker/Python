import datetime
from django.shortcuts import render, redirect
from .utils import get_token, search_artist, get_song, client_id, client_secret,SPOTIFY_REDIRECT_URI,auth_url,token_url
from django.http import HttpResponse
from django.conf import settings
import requests
import  urllib.parse

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
    scope = 'user-read-private user-read-email';
    prame={
      'response_type': 'code',
      'client_id': client_id,
      'scope': scope,
      'redirect_uri': SPOTIFY_REDIRECT_URI,
      'show_dilog': True
    }
    auth_url_me = f"{auth_url}?{urllib.parse.urlencode(prame)}"
    return redirect(auth_url_me)

def callback(request):
    print(request.GET)
    if 'error' in request.GET:    
        return render('profile/profile.html',{'error': request.args['error']})
    
    if 'code' in request.GET:
    
        authorization_code = request.GET.get('code') 
        print("authorization_code "+authorization_code)
        req_body={
            'code' : request.GET['code'],
            'grant_type':'authorization_code',
            'client_id': client_id,
            'client_secret': client_secret
        }
        
        response = requests.post(token_url, data=req_body)
        token_info = response.json()
        print(token_info)
        
        request.session['access_token'] = token_info['access_token']
        request.session['refresh_token']=token_info['refresh_token']
        request.session['expires_at']= datetime.now().timestamp() + token_info['expires_in']
        
        return render('profile/profile.html',{'info': session})
        # return HttpResponseRedirect('/profile/')