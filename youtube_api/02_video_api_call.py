from googleapiclient.discovery import build
import os


class YoutubeApi:

    def __init__(self, api_key):

        self.youtube_api = build("youtube", "v3", developerKey=api_key)

    def youtube_search(self, query):
        search_response = self.youtube_api.search().list(
            q=query,
            part="id,snippet",
            maxResults=10
        ).execute()

        video_ids = []
        for item in search_response.get("items", []):
            if item["id"]["kind"] == "youtube#video":
                video_ids.append(item["id"]["videoId"])
        return ",".join(video_ids)

    def video(self, video_ids):
        videos_list_response = self.youtube_api.videos().list(
            id=video_ids,
            part='snippet,statistics'
        ).execute()

        r = []
        for item in videos_list_response.get("items", []):
            print(item)
            r.append({"video_id":item['id'], "title":item["snippet"]["title"],
                      "channelTitle":item["snippet"]["channelTitle"],
                      "commentCount":item["statistics"]["commentCount"]})
        return r

    def comment(self, video_id, max_cnt=10):
        comment_list_response = self.youtube_api.commentThreads().list(
            videoId=video_id,
            part='id,replies,snippet',
            maxResults=max_cnt

        ).execute()

        for comment in comment_list_response.get("items", []):
            print(comment)



if __name__ == '__main__':
    DEVELOPER_KEY = os.getenv("YOUTUBE_API_KEY")
    api = YoutubeApi(DEVELOPER_KEY)
    video_ids = api.youtube_search("슈카월드")
    r_video = api.video(video_ids)
    # print(r_video)
    for item in r_video:
        print(item)
