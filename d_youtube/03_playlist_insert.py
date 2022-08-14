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
    maxResults=100
).execute()
channels = []
for result in get_channel_id.get("items", []):
    if result['id']['kind'] == "youtube#channel":
        print(result['id']['channelId'] + result['snippet']['title'])
        channels.append({result['snippet']['title']: result['id']['channelId']})

print(channels)
channel_id = channels[0]
print(channel_id)

# pl_list = []
# response = api_obj.playlists().list(
#     channelID=channel_id,
#     part='snippet',
#     maxResults=100
# ).execute()
#
# print(pl_list)

