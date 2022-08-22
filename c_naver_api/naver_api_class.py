import requests
from time import sleep
from urllib.parse import urlparse

class NaverApi():
    client_id = None
    client_secret = None

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def get_info(self, source):
        url = urlparse(source).geturl()
        print(url)
        result = requests.get(url,
                              headers={
                                  "X-Naver-Client-Id": self.client_id,
                                  "X-Naver-Client-Secret": self.client_secret
                              })
        print(result)
        return result.json()

    def blog(self, query, start=1, display=100):
        r = self.get_info(f"https://openapi.naver.com/v1/search/blog?query={query}&start={start}&display={display}")
        return r

    def get_repeat(self, quantity):
        # 10개면 10개씩 1번
        # 10000번이면 100개씩 100번
        repeat = quantity // 100  # quantity를 100으로 나눈만큼 돌아야 함
        display = 100
        # 100개씩 1000개
        if quantity < 100:
            display = quantity
            repeat = 1

        # 1, 101, 201, 301
        return (repeat, display)

    def cafe(self, query, quantity):
        # quantity만큼의 loop를 설계 해야 함
        # 10개면 10개씩 1번
        # 10000번이면 100개씩 100번
        repeat, display = self.get_repeat(quantity)
        for i in range(repeat):
            start = i * 100 + 1  # start는 최대 1000개까지 가능 스펙상 10만개까지 가능함
            r = self.get_info(f"https://openapi.naver.com/v1/search/cafearticle?query={query}&start={start}&display={display}")
            sleep(1)
            print(r)
        return r

if __name__ == '__main__':
    naver_api = NaverApi('0YWmAAZVcF4QBIAeYnu4', 'a7XyTYjawx')
    # 검색 건수를 넘기면 알아서 수집해줌
    cafe_r = naver_api.cafe("교대역 맛집", 10000)
    for cafe in cafe_r:
        print(cafe)

