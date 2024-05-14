from django.shortcuts import render
from ytmusicapi import YTMusic

ytmusic = YTMusic()

def index(request):
    return render(request,'index.html')

def get_song(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        search_results = ytmusic.search(name)
        return render(request, 'index.html',{'results' : search_results})
    return render(request, 'index.html')

def clicked(request, id):
    artist = ytmusic.get_artist(id)
    return render(request,'artist.html', {'artist':artist})