import googleapiclient.discovery
from googleapiclient.discovery import build
import googleapiclient.errors
import google_auth_oauthlib.flow
import os
from video_info import YoutubeApi

api_key = os.getenv("YOUTUBE_API_KEY")

youtube_api = YoutubeApi(api_key)

api_obj = build('youtube', 'v3', developerKey=api_key)
api_server_name = "youtube"
# 웹 어플리케이션
# client_secrets_file = "client_secret_web.json"
# 데스크톱 어플리케이션
client_secrets_file = "client_secret_desktop.json"
scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    client_secrets_file, scopes
)
credentials = flow.run_console()


def get_video_comments(q):
    v_list = youtube_api.get_videos_list(q)
    v_id = list(v_list[0].values())[0]
    v_comments = api_obj.commentThreads().list(
        part='snippet,replies',
        videoId=v_id,
        maxResults=10).execute()
    for result in v_comments.get('items', []):
        print(result['snippet']['topLevelComment']['snippet']['textDisplay'])


def insert_video_comment(q, text):
    v_list = youtube_api.get_videos_list(q)
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

