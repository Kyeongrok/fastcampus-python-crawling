from googleapiclient.discovery import build
import os, json
import pandas as pd


class YoutubeApi:

    def __init__(self, api_key):

        self.youtube_api = build("youtube", "v3", developerKey=api_key)

    def video_search_list(self, query, max_results=10):
        search_response = self.youtube_api.search().list(
            q=query,
            part="id,snippet",
            maxResults=max_results
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
            part='replies,snippet',
            maxResults=max_cnt

        ).execute()
        comments = []
        for comment in comment_list_response.get("items", []):
            # print(comment)
            snippet = comment['snippet']['topLevelComment']['snippet']
            map = {"link":f"https://www.youtube.com/watch?v={snippet['videoId']}", "videoId":snippet["videoId"], "textOriginal":snippet['textOriginal'], "authorDisplayName":snippet['authorDisplayName']}
            comments.append(map)
            # print(json.dumps(comment))
        return comments

    def save_to_excel(self, search_results, filename):
        df = pd.DataFrame(search_results)
        df.to_excel(filename)

    def crawl_comment_by_keyword(self, keyword, video_cnt=5):
        video_ids = self.video_search_list(keyword, video_cnt)
        r_video = self.video(video_ids)
        l = []
        for video in r_video:
            cnt = int(video['commentCount'])
            if cnt > 100:
                cnt = 100
            comment_list = self.comment(video['video_id'], cnt)
            l += comment_list
        return l



if __name__ == '__main__':
    DEVELOPER_KEY = os.getenv("YOUTUBE_API_KEY")
    api = YoutubeApi(DEVELOPER_KEY)

    # comment_results = api.comment("-B1g8tFC6Bg", 61)
    keyword = "핸드크림"
    l = api.crawl_comment_by_keyword(keyword, 10)
    api.save_to_excel(l, f"{keyword}.xlsx")
