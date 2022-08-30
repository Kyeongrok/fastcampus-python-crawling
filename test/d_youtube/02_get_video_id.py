from googleapiclient.discovery import build
import os


class YoutubeApi:

    def __init__(self, api_key):
        self.youtube_api = build('youtube', 'v3', developerKey=api_key)

    def call_search_api(self, q):
        search_result = self.youtube_api.search().list(
            q=q,
            order='relevance',
            part='snippet',
            maxResults=10
        ).execute()
        ids = []
        for result in search_result.get('items', []):
            print(result)
            if result['id']['kind'] == "youtube#video":
                ids.append(result['id']['videoId'])
        return ",".join(ids)

    def get_video_infos(self, video_ids):

        video_infos = self.youtube_api.videos().list(
            part='snippet, statistics',
            id=video_ids,
        ).execute()
        for result in video_infos.get('items', []):
            print('videoInfo:', result['id'], result['statistics']['commentCount'])


api_key = os.getenv("YOUTUBE_API_KEY")
api = YoutubeApi(api_key)
ids = api.call_search_api("게임")
print(ids)
print(api.get_video_infos(ids))
