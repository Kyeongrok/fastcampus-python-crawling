from googleapiclient.discovery import build
import os

api_key = os.getenv("YOUTUBE_API_KEY")
# 내 채널 id
channel_q = "girl's generation"
channel_title = ''
channel_id = ''
playlist_id = ''

api_obj = build('youtube', 'v3', developerKey=api_key)
get_channel_id = api_obj.search().list(
    q=channel_q,
    order='relevance',
    part='snippet',
    maxResults=10
).execute()
channels = []
for result in get_channel_id.get("items", []):
    if result['id']['kind'] == "youtube#channel":
        print(result['id']['channelId'] + result['snippet']['title'])
        channels.append({result['snippet']['title']: result['id']['channelId']})
        channel_id = result['id']['channelId']

print(channels)
print(channel_id)

pl_list = []
response = api_obj.playlists().list(
    channelId=channel_id,
    part='snippet',
    maxResults=10
).execute()

print(response)

