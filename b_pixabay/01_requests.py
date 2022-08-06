import requests


def crawl(url):
    data = requests.get(url)
    print(data, url)
    return data.content


url = "https://www.instagram.com/explore/tags/%EC%95%84%EC%9D%B4%EC%9C%A0/"

pageString = crawl(url)
print(pageString)
