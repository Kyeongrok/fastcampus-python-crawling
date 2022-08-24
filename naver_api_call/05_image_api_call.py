import requests
import os

from urllib.request import Request, urlopen


class NaverSearchApi():

    api_url = "https://openapi.naver.com/v1/search/blog.json"

    def call_api(self, keyword, start=1, display=10):
        url = f"{self.api_url}?query={keyword}&start={start}&display={display}"
        res = requests.get(url, headers={"X-Naver-Client-Id": "wpmE0jjCJzOcHzV5i0kB",
                                         "X-Naver-Client-Secret":"71r4yWsPE5"})
        print(res)
        r = res.json()
        return r

    def get_paging_call(self, keyword, quantity):
        if quantity > 1100:
            # quantity = 1100
            exit("Error 최대 요청할 수 있는 건수는 1100건 입니다.")

        repeat = quantity // 100 # 1000총 10번
        display = 100
        if quantity < 100:
            display = quantity
            repeat = 1

        result = []
        for i in range(repeat):
            start = i * 100 + 1
            # 101
            if start > 1000:
                start = 1000
            print(f"{i + 1}번 반복 합니다. start:{start}")
            r = self.call_api(keyword, start=start, display=display)
            print(r['items'][0])
            result += r['items']
        return result

    def blog(self, keyword, quantity=100):
        self.api_url = "https://openapi.naver.com/v1/search/blog.json"
        return self.get_paging_call(keyword, quantity)

    def news(self, keyword, quantity=100):
        self.api_url = "https://openapi.naver.com/v1/search/news.json"
        return self.get_paging_call(keyword, quantity)

    def webkr(self, keyword, quantity=100):
        self.api_url = "https://openapi.naver.com/v1/search/webkr.json"
        return self.get_paging_call(keyword, quantity)

    def image(self, keyword, quantity=100):
        self.api_url = "https://openapi.naver.com/v1/search/image.json"
        return self.get_paging_call(keyword, quantity)

    def save_images(self, path, search_result):
        if not os.path.exists(path):
            os.mkdir(path)
        else:
            exit(f"'{path}' 디렉토리가 이미 존재 합니다.")

        cnt = 1
        for item in search_result:
            try:
                image_url = item['link']
                image_byte = Request(image_url, headers={'User-Agent': 'Mozilla/5.0'})
                filename = image_url.split("/")[-1]
                f = open(f"{path}/{cnt}.jpg", "wb")
                f.write(urlopen(image_byte).read())
                f.close()
                cnt+=1
            except Exception as e:
                print(e)

if __name__ == '__main__':
    naver_search_api = NaverSearchApi()
    keyword = "헬스장"
    r = naver_search_api.image(keyword, 200)
    # print(r)
    print(r)
    naver_search_api.save_images(keyword, r)
