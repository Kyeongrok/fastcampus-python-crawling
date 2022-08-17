import requests
from bs4 import BeautifulSoup

data = requests.get("https://www.ev.or.kr/portal/localInfo")
file = open("ev_or_kr_local_info.html", "w+")
file.write(data.text)