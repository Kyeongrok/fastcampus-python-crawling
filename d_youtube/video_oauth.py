# api프로젝트 만들고
# api프로젝트에서 youtube data api
# 1. 검색어를 넣어서 video, channel 정보 가져오기
# 2. videoId를 하나 정해서 댓글, 좋아요 가져오기
# 3. channelId로 재생목록 가져오기
# 4. 내 채널에서 재생목록 생성하기

from googleapiclient.discovery import build
from google_auth_oauthlib import flow
import os, json


class YoutubeApi:
    youtube_api = None
    youtube_auth_api = None
    secret_filename = ""

    def __init__(self, api_key, secret_filename):
        self.youtube_api = build('youtube', 'v3', developerKey=api_key)
        self.secret_filename = secret_filename

    def set_youtube_auth_api(self):
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
        scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
        flow_obj = flow.InstalledAppFlow.from_client_secrets_file(
            self.secret_filename, scopes
        )
        credentials = flow_obj.run_local_server()
        self.youtube_auth_api = build(
            "youtube", "v3", credentials=credentials
        )

    def get_channel_info(self, q):
        search_list = self.youtube_api.search().list(
            q=q,
            order='relevance',
            part='snippet',
            maxResults=10
        ).execute()
        channels = {}
        for result in search_list.get('items', []):
            # print(result)
            if result['id']['kind'] == "youtube#channel":
                print(result)
                channels[result['snippet']['title']] = result['id']['channelId']
        # print(channels)
        channels_id = list(channels.keys())[0]
        channels_title = list(channels.values())[0]
        return [channels_id, channels_title]

    def get_videos_list(self, q):
        get_list = self.youtube_api.search().list(
            q=q,
            order='relevance',
            part='snippet',
            maxResults=10
        ).execute()
        print(get_list)
        videos = []
        for result in get_list.get('items', []):
            # print(result)
            if result['id']['kind'] == "youtube#video":
                # print(result['id'])
                # print(result['id']['videoId'] + result['snippet']['title'])
                video_id = result['id']['videoId']
                print('video_id:', video_id)
                videos.append({result['snippet']['title']: video_id})
        return videos

    def get_video_info(self, video_id):
        video_lifo = self.youtube_api.videos().list(
            part='snippet, statistics',
            id=video_id,
        ).execute()
        infos = []
        result = video_lifo.get('items', [])[0]
        print(result['snippet']['title'] + ' ' + result['snippet']['channelId'])
        print(result['statistics']['viewCount'])
        print(result['statistics']['likeCount'])
        print(result['statistics']['commentCount'])
        infos.append(result['snippet']['title'])
        infos.append(result['snippet']['channelId'])
        infos.append(result['statistics']['viewCount'])
        infos.append(result['statistics']['likeCount'])
        infos.append(result['statistics']['commentCount'])

    def get_video_comments(self, v_id):
        v_comments = self.youtube_api.commentThreads().list(
            part='snippet,replies',
            videoId=v_id,
            maxResults=10).execute()

        r = []
        items = v_comments.get('items', [])
        print('items:', json.dumps(items))
        for result in items:
            snippet = result['snippet']['topLevelComment']['snippet']
            r.append({"authorDisplayName": snippet['authorDisplayName'], "textDisplay": snippet['textDisplay']})

        return r

    def send_comment(self, v_id, text):
        if self.youtube_auth_api is None:
            self.set_youtube_auth_api()

        insert_comment = self.youtube_auth_api.commentThreads().insert(
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

    def get_playlist(self, ch_id):
        pl_list = []
        response = self.youtube_api.playlists().list(
            channelId=ch_id,
            part='snippet',
            maxResults=10
        ).execute()
        print(response)


if __name__ == '__main__':
    api_key_1 = os.getenv("YOUTUBE_API_KEY")
    api = YoutubeApi(api_key=api_key_1, secret_filename="client_secret_rrr.json")
    # v_list = api.get_videos_list('슈카월드')
    # play_lists = api.get_playlist("")
    r = api.get_channel_info("")
    print(r)
