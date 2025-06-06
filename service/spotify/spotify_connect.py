import spotipy
from spotipy import SpotifyClientCredentials
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv()

class SpotifyAuthManage:
    def __init__(self):
        self.client_id = os.getenv('SPOTIFY_CLIENT_ID')
        self.client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')

        # Client Credentials 방식 (브라우저 인증 불필요)
        client_credentials_manager = SpotifyClientCredentials(
            client_id=self.client_id,
            client_secret=self.client_secret
        )

        self.sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        print("✅ Spotify 공개 API 연결 완료!")


    def get_spotify_object(self):
        return self.sp

    def search_track(self, query, limit=10):
        """곡 검색"""
        try:
            results = self.sp.search(q=query, type='track', limit=limit)
            tracks = []
            for track in results['tracks']['items']:
                tracks.append({
                    'name': track['name'],
                    'artist': ', '.join([artist['name'] for artist in track['artists']]),
                    'album': track['album']['name'],
                    'id': track['id']
                })
            return tracks
        except Exception as e:
            print(f"검색 실패: {e}")
            return []

    def get_track_info(self, track_id):
        """특정 곡 정보"""
        try:
            track = self.sp.track(track_id)
            return {
                'name': track['name'],
                'artist': ', '.join([artist['name'] for artist in track['artists']]),
                'album': track['album']['name'],
                'duration': track['duration_ms'] // 1000,
                'popularity': track['popularity']
            }
        except Exception as e:
            print(f"곡 정보 가져오기 실패: {e}")
            return None