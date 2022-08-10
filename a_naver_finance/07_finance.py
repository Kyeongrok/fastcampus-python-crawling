import bs4
import requests
# find, select 사용법
Url = "https://finance.naver.com/item/main.naver?code=005930"
Html = requests.get(Url)

bsObj = bs4.BeautifulSoup(Html.text, "html.parser")
print(bsObj.title)
print(bsObj.a.get('href'))
print(bsObj.get_text())
