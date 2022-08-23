import requests

def call_api(keyword, start=1, display=10):
    url = f"https://openapi.naver.com/v1/search/blog.json?query={keyword}&start={start}&display={display}"
    res = requests.get(url, headers={"X-Naver-Client-Id": "wpmE0jjCJzOcHzV5i0kB",
                                     "X-Naver-Client-Secret":"71r4yWsPE5"})
    print(res)
    r = res.json()
    return r


def get_paging_call(keyword, quantity):
    if quantity > 1100:
        # quantity = 1100
        exit("Error 최대 요청할 수 있는 건수는 1100건 입니다.")

    repeat = quantity // 100 # 1000총 10번
    result = []
    for i in range(repeat):
        start = i * 100 + 1
        # 101
        if start > 1000:
            start = 1000
        print(f"{i + 1}번 반복 합니다. start:{start}")
        r = call_api(keyword, start=start, display=100)
        print(r['items'][0])
        result += r['items']
    return result


if __name__ == '__main__':
    r = get_paging_call("강남역 사건사고", 1100)
    print(r[0])
    print(len(r))
