from service.spotify.spotify_connect import SpotifyAuthManage
from service.youtube.youtube_connect import ConnectYoutube
from service.generate_vector.compute_similarity import get_similarity
if __name__ == "__main__":
    spotify_object = SpotifyAuthManage()
    search_results = spotify_object.search_track("뉴진스", limit=1)
    youtube_object = ConnectYoutube()

    first_track = search_results[0]  # ✅ 수정됨
    search_query = f"{first_track['artist']} {first_track['name']} official"
    print(search_query)

    result = youtube_object.search_videos(search_query)
    print(result)
    '''
    print("서버가 실행됨")
    y_text = "NewJeans  How Sweet Official MV" # youtube
    y_text0 = "NewJeans How Sweet Dance Practice"
    y_text1 = "NewJeans Hype boy Official MV"
    y_text2 = "NewJeans Attention Official MV"
    s_text = "NewJeans How Sweet official" # spotify
    result = get_similarity()
    compare_y = result.get_embedding(y_text)
    compare_y0 = result.get_embedding(y_text0)
    compare_y1 = result.get_embedding(y_text1)
    compare_y2 = result.get_embedding(y_text2)
    compare_s = result.get_embedding(s_text)
    print(f"cosine 유사도 비교 용, 뉴진스 how sweet, how sweet: {result.cosine_similarity(compare_s, compare_y)}")
    print(f"cosine 유사도 비교 용, 뉴진스 how sweet, how sweet dance Practice: {result.cosine_similarity(compare_s, compare_y0)}")
    print(f"cosine 유사도 비교 용, 뉴진스 how sweet, hype boy: {result.cosine_similarity(compare_s, compare_y1)}")
    print(f"cosine 유사도 비교 용, 뉴진스 how sweet, attention: {result.cosine_similarity(compare_s, compare_y2)}")
    print(f"cosine 유사도 비교 용, 뉴진스 how sweet, attention: {result.cosine_similarity(compare_s, compare_y2)}")

    print(f"cosine 거리 : {result.cosine_distance(compare_s, compare_y)}")'''
