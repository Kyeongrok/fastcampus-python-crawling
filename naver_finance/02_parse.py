import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/item/main.naver?code=005930"
res = requests.get(url)
bsobj = BeautifulSoup(res.text, "html.parser")

div_today = bsobj.find("div", {"class":"today"})
em = div_today.find("em")
price = em.find("span", {"class":"blind"}).text
print(price)




