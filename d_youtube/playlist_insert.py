from googleapiclient.discovery import build
import googleapiclient.errors
import google_auth_oauthlib.flow
from video_info import get_channel_info
import video_info
import os

# 내 채널 id
channel_q = "girl's generation"
client_secrets_file = "client_secret_488418297-otapo0hisu0kvje6fp9s6l2s502n6024.apps.googleusercontent.com.json"
scopes = "https://www.googleapis.com/auth/youtube"
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    client_secrets_file, scopes
)
credentials = flow.run_console()
api_key = os.getenv("YOUTUBE_API_KEY")
api_obj = build('youtube', 'v3', developerKey=api_key)
youtube = googleapiclient.discovery.build(
    'youtube', 'v3', credentials=credentials
)


def get_playlist(ch_id):
    pl_list = []
    response = api_obj.playlists().list(
        channelId=ch_id,
        part='snippet',
        maxResults=10
    ).execute()
    print(response)


def insert_playlist():
    insert_response = youtube.playlists().insert(
        part="snippet, status",
        body={
            "snippet": {
                "title": "python으로 만든 플레이리스트",
                "description": "초보자도 가능한 플레이리스트",
            },
            "status": {
                "privacyStatus": "private"
            }
        }
    ).execute()
    print(insert_response["id"])
    return insert_response["id"]


def insert_playlist_item(pl_id, search):
    v_list = video_info.get_videos_list(search)
    v_id = list(v_list[0].values())[0]
    insert_response = youtube.playlistItems().insert(
        part='snippet, contentDetails, status',
        body={
            "snippet": {
                "playlistId": pl_id,
                "resourceId": {
                    "kind": "youtube#video",
                    "videoId": v_id
                }
            }
        }
    ).execute()
    print(insert_response)


def delete_playlist(dl_id):
    delete_response = youtube.playlistItems().delete(
        id="UExMb2FkNnhMTzZmRWFXODY4MUhQSXFaaGNvMlVGbUZ4UC41NkI0NEY2RDEwNTU3Q0M2"
    ).execute()
    print(delete_response)


if __name__ == '__main__':
    # channel_id = get_channel_info("girl's generation")[1]
    # get_playlist(channel_id)
    # playlist_id = insert_playlist()
    # tmp_id = "PLLoad6xLO6fEaW8681HPIqZhco2UFmFxP"
    # insert_playlist_item(tmp_id, "girl's generation")
    delete_id = "UExMb2FkNnhMTzZmRWFXODY4MUhQSXFaaGNvMlVGbUZ4UC41NkI0NEY2RDEwNTU3Q0M2"
    delete_playlist(delete_id)



