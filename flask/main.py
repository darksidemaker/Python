import datetime
import os
# import requests
import urllib

from flask import Flask, jsonify, redirect, request, session

app = Flask(__name__)
app.secret_key = '53d355f8-571a-4590-a310-1f9579440851'

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
# REDIRECT_URI = 'https://refactored-winner-p459g9p7p7x2g7g-8000.app.github.dev/callback'
REDIRECT_URI = 'http://localhost:8000/callback'

AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL= 'https://accounts.spotify.com/api/token'
API_BASE_URL = 'https://api.spotify.com/v1/'

@app.route('/')
def index():
    return "<a href='/login'>cLick me</a>"
    
    
@app.route('/login')
def login():
    scope = 'user-read-private user-read-email'
    params={
      'client_id': CLIENT_ID,
      'response_type': 'code',
      'scope': scope,
      'redirect_uri': REDIRECT_URI,
      'show_dialog': True
    }
    auth_url_me = f"{AUTH_URL}?{urllib.parse.urlencode(params)}"

    return redirect(auth_url_me)

@app.route('/callback')
def callback():
    if 'error' in request.args:
     return jsonify({"error": request.args['error']})

    if 'code' in request.args:
        req_body = {
            'code': request.args['code'],
            'grant_type': 'authorization_code',
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET
        }

    response = request.post(TOKEN_URL, data=req_body)
    token_info = response. json()

    session['access_token'] = token_info['access_token']
    session['refresh_token'] = token_info['refresh_token']
    session['expires_at'] = datetime.now().timestamp() + token_info['expires_in']

    return redirect('/playlists')

@app.route('/playlists')
def get_playlists():
    if 'access_token' not in session:
        return redirect('/login')

    if datetime.now().timestamp() > session['expires_at']:
        return redirect('/refresh-token')

        headers = {
                'Authorization': f"Bearer {session['access_token']}"}
  
        response = requests.get(API_BASE_URL + 'me/playlists', headers=headers)
        playlists = response. json()

        return jsonify(playlists)

@app.route('/refresh-token')
def refresh_token():
    if 'refresh_token' not in session:
        return redirect('/login')

    if datetime.now().timestamp() > session['expires_at']:
        req_body = {
            'grant_type': 'refresh_token',
            'refresh_token': session['refresh_token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET
        }
    
        response = request.post(TOKEN_URL, data=req_body)
        new_token_info = response. json()

        session['access_token'] = new_token_info['access_token']
        session['expires_at'] = datetime.now(). timestamp() + new_token_info['expires_in']

        return redirect('/playlists')
    
if __name__ == ' __main__ ':
    app.run(host='0.0.0.0', debug=True)