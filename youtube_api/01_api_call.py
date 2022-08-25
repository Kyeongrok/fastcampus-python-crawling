from googleapiclient.discovery import build
import os

DEVELOPER_KEY = os.getenv("YOUTUBE_API_KEY")


def youtube_search(query):
    youtube_api = build("youtube", "v3", developerKey=DEVELOPER_KEY)
    search_response = youtube_api.search().list(
        q=query,
        part="id,snippet",
        maxResults=10
    ).execute()

    for item in search_response.get("items", []):
        print(item)

if __name__ == '__main__':
    youtube_search("업무 자동화")