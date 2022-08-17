import os
import sys
import urllib.request
from urllib.parse import urlparse
import requests
from naver_api import get_info

clientId = '0YWmAAZVcF4QBIAeYnu4'
clientSecret = 'a7XyTYjawx'
keyword = "맛집"
url = "https://openapi.naver.com/v1/search/image?query="
image_list = []
path = 'naver_crawl_imgs'
info = get_info(url, keyword, clientId, clientSecret)
for item in info.get('items', []):
    print(item['link'])
    image_list.append(item['link'])

try:
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        print('이미 폴더가 존재 합니다.')
        sys.exit(0)
except OSError:
    print(OSError)
    sys.exit(0)
for img in image_list:
    req = urllib.request.Request(img, headers={'User-Agent': 'Mozila/5.0'})
    filename = img.split('/')[-1]
    savaPath = path+'/'+filename
    f = open(savaPath, 'wb')
    f.write(urllib.request.urlopen(req).read())
    f.close()

