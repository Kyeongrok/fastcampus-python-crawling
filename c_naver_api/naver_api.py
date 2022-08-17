import os
import sys
from urllib.parse import urlparse
import requests
clientId = '0YWmAAZVcF4QBIAeYnu4'
clientSecret = 'a7XyTYjawx'
keyword = "소녀시대"


def get_info(u, q, i, s):
    source = u + q  # json 형식
    result = requests.get(urlparse(source).geturl(),
                          headers={
                              "X-Naver-Client-Id": i,
                              "X-Naver-Client-Secret": s
                          })
    print(result.json())
    return result.json()


if __name__ == "__main__":
    url_arr = ["https://openapi.naver.com/v1/search/blog?query=",
               "https://openapi.naver.com/v1/search/cafearticle?query=",
               "https://openapi.naver.com/v1/search/image?query=",
               "https://openapi.naver.com/v1/search/shop?query"
               ]
    for url in url_arr:
        get_info(url, keyword, clientId, clientSecret)
