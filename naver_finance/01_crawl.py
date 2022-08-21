import requests

url = "https://finance.naver.com/item/main.naver?code=005930"
res = requests.get(url)
print(res.text)



