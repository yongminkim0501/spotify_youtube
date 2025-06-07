from service.spotify.spotify_connect import SpotifyAuthManage
from service.youtube.youtube_connect import ConnectYoutube

if __name__ == "__main__":
    spotify_object = SpotifyAuthManage()
    search_results = spotify_object.search_track("아이유", limit=5)
    youtube_object = ConnectYoutube()

    first_track = search_results[0]  # ✅ 수정됨
    search_query = f"{first_track['artist']} {first_track['name']}"
    print(search_query)

    result = youtube_object.search_videos(search_query)
    print(result)

