from googleapiclient.discovery import build
import os

api_key = os.getenv("YOUTUBE_API_KEY")
print(api_key)
playlist_id = 'PLLoad6xLO6fHniD8UaLpaPdWA1Nv_ZTa3'
channel_id = 'UCt15X5eHLwyP8PpNtQTkuDQ'


comments = list()
api_obj = build('youtube', 'v3', developerKey=api_key)
response = api_obj.search().list(
    q="Official Dopa",
    order='relevance',
    part='snippet',
    maxResults=50
).execute()
playlists = api_obj.playlists().list(
    channelId=channel_id,
    part='snippet',
    maxResults=100
).execute()

print(len(playlists))
print(playlists['items'])