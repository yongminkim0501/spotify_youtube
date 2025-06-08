from dotenv import load_dotenv
import os
from googleapiclient.discovery import build


load_dotenv()

class ConnectYoutube:
    def __init__(self):
        self.youtube_key = os.getenv("YOUTUBE_KEY")
        self.youtube = build('youtube', 'v3', developerKey=self.youtube_key)

    def search_videos(self,query):
        request = self.youtube.search().list(
            part="snippet",
            maxResults=1,
            q=query,
            type="video"
        )
        response = request.execute()
        return response

    def get_search_name(self, query):
        data = self.search_videos(query)
        return data