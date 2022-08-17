from bs4 import BeautifulSoup

# if __name__ == "__main__":
html_text = open("ev_or_kr_local_info.html").read()
bsobj = BeautifulSoup(html_text, "html.parser")

table = bsobj.find("table", {"class":"table_02_2_1"})
tbody = table.find("tbody")
trs = tbody.find_all("tr")
tr = trs[0]
tds = tr.find_all("td")
print(tds[2].text) # 민간공고대수
print(tds[3].text) # 접수대수
print(tds[4].text) # 출고대수
print(tds[5].text) # 출고잔여대수
