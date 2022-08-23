import googleapiclient.discovery
from googleapiclient.discovery import build
import googleapiclient.errors
import google_auth_oauthlib.flow
import os
from video_info import YoutubeInfoApi


# 데스크톱 어플리케이션
class YoutubeCommentApi():
    client_secrets_file = "client_secret_desktop.json"

    def __init__(self, client_secret_filename):
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
        self.client_secrets_file = client_secret_filename
        scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            self.client_secrets_file, scopes
        )
        self.credentials = flow.run_local_server()

    def send_comment(self, v_id, text):
        youtube = googleapiclient.discovery.build(
            "youtube", "v3", credentials=self.credentials
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
    api_key = os.getenv("YOUTUBE_API_KEY")
    youtube_api = YoutubeInfoApi(api_key)
    youtube_comment_api = YoutubeCommentApi("client_secret_rrr.json")
    query = "슈카월드"
    v_id = "RGLvq6PNXGo"
    # youtube_comment_api.send_comment(v_id, '흥미롭군요 ㅎㅎㅎㅎ')
    r = youtube_api.get_video_comments(v_id)
    for item in r:
        print(item)
