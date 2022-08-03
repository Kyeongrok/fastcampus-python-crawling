import bs4
from bs4 import BeautifulSoup

html = "<html><div></div></html>"
bsObj = bs4.BeautifulSoup(html, "html.parser")

print(type(bsObj))
print(bsObj)
