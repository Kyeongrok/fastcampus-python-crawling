# api프로젝트 만들고
# api프로젝트에서 youtube data api
# 1. 검색어를 넣어서 video, channel 정보 가져오기
# 2. videoId를 하나 정해서 댓글, 좋아요 가져오기
# 3. channelId로 재생목록 가져오기
# 4. 내 채널에서 재생목록 생성하기

from googleapiclient.discovery import build
import os

api_key = os.getenv("YOUTUBE_API_KEY")
api_obj = build('youtube', 'v3', developerKey=api_key)


def get_channel_info(q):
    get_search_list = api_obj.search().list(
        q=q,
        order='relevance',
        part='snippet',
        maxResults=10
    ).execute()
    channels = {}
    for result in get_search_list.get('items', []):
        # print(result)
        if result['id']['kind'] == "youtube#channel":
            # print(result['id'])
            # print(result['id']['channelId'] + result['snippet']['title'])
            channels[result['snippet']['title']] = result['id']['channelId']
    # print(channels)
    channels_id = list(channels.keys())[0]
    channels_title = list(channels.values())[0]
    return [channels_id, channels_title]


def get_videos_list(q):
    get_list = api_obj.search().list(
        q=q,
        order='relevance',
        part='snippet',
        maxResults=10
    ).execute()
    videos = []
    for result in get_list.get('items', []):
        # print(result)
        if result['id']['kind'] == "youtube#video":
            # print(result['id'])
            # print(result['id']['videoId'] + result['snippet']['title'])
            videos.append({result['snippet']['title']: result['id']['videoId']})
    return videos


def get_video_info(i):
    video_lifo = api_obj.videos().list(
        part='snippet, statistics',
        id=i,
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


if __name__ == '__main__':
    # print(get_channel_info("girl's generation"))
    # channel_id = get_channel_info("girl's generation")[0]
    v_list = get_videos_list('슈카월드')
    # 첫번째 videoId 가져오기
    v_id = list(v_list[0].values())[0]
    get_video_info(v_id)
    # print(v_list)
    # print(list(v_list[0].values()))
