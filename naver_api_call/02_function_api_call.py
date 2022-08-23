import requests

def call_api(keyword, start=1, display=10):
    url = f"https://openapi.naver.com/v1/search/blog.json?query={keyword}&start={start}&display={display}"
    res = requests.get(url, headers={"X-Naver-Client-Id": "wpmE0jjCJzOcHzV5i0kB",
                                     "X-Naver-Client-Secret":"71r4yWsPE5"})
    print(res)
    r = res.json()
    return r

def get_paging_call(keyword, quantity):
    repeat = 9 # 1000총 10번
    for i in range(repeat):
        print(f"{i + 1}번 반복 합니다")


if __name__ == '__main__':
    # 1100
    # r = call_api("교대역 병원", 1, 100)
    r = get_paging_call("교대역 이비인후과", 900)
