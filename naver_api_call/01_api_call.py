import requests

# 1, 101, 201, 301 ... 901, 1000
url = "https://openapi.naver.com/v1/search/blog.json?query=교대역 맛집&start=1000&display=100"
res = requests.get(url, headers={"X-Naver-Client-Id": "wpmE0jjCJzOcHzV5i0kB",
                                 "X-Naver-Client-Secret":"71r4yWsPE5"})
print(res)
r = res.json()
print(len(r['items']))
# for item in r['items']:
#     print(item)
