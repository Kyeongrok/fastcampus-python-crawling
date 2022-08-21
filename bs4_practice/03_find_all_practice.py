from bs4 import BeautifulSoup

f = open("02_ul_li.html", encoding="utf-8")
bsobj = BeautifulSoup(f.read(), "html.parser")
ul = bsobj.find("ul")
lis = ul.find_all("li")
for li in lis:
    print(li.text)
