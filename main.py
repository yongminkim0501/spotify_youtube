from service.spotify.spotify_connect import SpotifyAuthManage
if __name__ == "__main__":
    Spotify_Object = SpotifyAuthManage()
    search_results = Spotify_Object.search_track("아이유", limit=5)
    #for track in search_results:
        #print(f"🎵 {track['name']} - {track['artist']}")
    print(search_results)