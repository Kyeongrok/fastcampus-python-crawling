
import requests
from bs4 import BeautifulSoup
url = "https://pixabay.com/images/search/%EA%B2%8C%EC%9E%84/?pagi=3"
url = 'https://pixabay.com/ko/images/search/%EA%B0%95%EC%95%84%EC%A7%80/?pagi=3'

res = requests.get(url)

bsobj = BeautifulSoup(res.text, "html.parser")

print(bsobj)
