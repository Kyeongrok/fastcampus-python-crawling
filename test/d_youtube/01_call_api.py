from googleapiclient.discovery import build
import os
api_key = os.getenv("YOUTUBE_API_KEY")
youtube_api = build('youtube', 'v3', developerKey=api_key)


def call_search_api(q):
    search_result = youtube_api.search().list(
        q=q,
        order='relevance',
        part='snippet',
        maxResults=10
    ).execute()
    for result in search_result.get('items', []):
        print(result)

call_search_api("게임")
