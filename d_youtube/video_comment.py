import googleapiclient.discovery
from googleapiclient.discovery import build
import googleapiclient.errors
import google_auth_oauthlib.flow
import os
from video_info import get_videos_list
api_key = os.getenv("YOUTUBE_API_KEY")
api_obj = build('youtube', 'v3', developerKey=api_key)
api_server_name = "youtube"
# 웹 어플리케이션
# client_secrets_file = "client_secret_488418297-7tidrd0nl86hqrdti3parb2d6rdbjb1f.apps.googleusercontent.com (4).json"
# 데스크톱 어플리케이션
client_secrets_file = "client_secret_488418297-otapo0hisu0kvje6fp9s6l2s502n6024.apps.googleusercontent.com.json"
scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    client_secrets_file, scopes
)
credentials = flow.run_console()


def get_video_comments(q):
    v_list = get_videos_list(q)
    v_id = list(v_list[0].values())[0]
    v_comments = api_obj.commentThreads().list(
        part='snippet,replies',
        videoId=v_id,
        maxResults=10).execute()
    for result in v_comments.get('items', []):
        print(result['snippet']['topLevelComment']['snippet']['textDisplay'])


def insert_video_comment(q, text):
    v_list = get_videos_list(q)
    v_id = list(v_list[0].values())[0]
    youtube = googleapiclient.discovery.build(
        api_server_name, "v3", credentials=credentials
    )
    insert_comment = youtube.commentThreads().insert(
        part='snippet',
        body={
            "snippet": {
                "videoId": v_id,
                "topLevelComment": {
                    "snippet": {
                        "textOriginal": text
                    }
                }
            }
        }
    )
    response = insert_comment.execute()
    print(response)


if __name__ == '__main__':
    insert_video_comment('슈카월드', '유익한 내용 이네요.')
    get_video_comments('슈카월드')


#     for item in comments['items']:
#         comment = item['snippet']['topLevelComment']['snippet']
#         comments.append(
#             [comment['textDisplay'], comment['authorDisplayName'], comment['publishedAt'], comment['likeCount']])
#         if item['snippet']['totalReplyCount'] > 0:
#             for reply_item in item['replies']['comments']:
#                 reply = reply_item['snippet']
#                 comments.append(
#                     [reply['textDisplay'], reply['authorDisplayName'], reply['publishedAt'], reply['likeCount']])
#
#     if 'nextPageToken' in comments:
#         response = api_obj.commentThreads().list(part='snippet,replies', videoId=v_id,
#                                                  pageToken=comments['nextPageToken'], maxResults=10).execute()
#     else:
#         break
#
# print(comments)

# comments = list()
# playlists = api_obj.playlists().list(
#     channelId=channel_id,
#     part='snippet',
#     maxResults=100
# ).execute()
# print(len(playlists))
# print(playlists['items'])