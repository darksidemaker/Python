from ytmusicapi import YTMusic

ytmusic = YTMusic() 
# from ytmusicapi import YTMusic
# ytmusic = YTMusic("oauth.json")
# playlistId = ytmusic.create_playlist("test", "test description")
search_results = ytmusic.search("Oasis Wonderwall")
print(search_results[1]['videoId'])
# ytmusic.add_playlist_items(playlistId, [search_results[1]['videoId']])