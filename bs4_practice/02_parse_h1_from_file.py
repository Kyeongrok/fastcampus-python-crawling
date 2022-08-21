from bs4 import BeautifulSoup

f = open("01_h1_tag.html", encoding="utf-8")

bsobj = BeautifulSoup(f.read(), "html.parser")

h1 = bsobj.find("h1")
p = bsobj.find("p")
h2 = bsobj.find("h2")

print(h1.text)
print(p.text)
print(h2.text)
