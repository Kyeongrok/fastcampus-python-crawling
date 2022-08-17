from bs4 import BeautifulSoup

# if __name__ == "__main__":
html_text = open("ev_or_kr_local_info.html").read()
bsobj = BeautifulSoup(html_text, "html.parser")

table = bsobj.find("table", {"class":"table_02_2_1"})
tbody = table.find("tbody")
trs = tbody.find_all("tr")
tr = trs[0]
tds = tr.find_all("td")

replace_brackets = lambda x: x.replace("(", "").replace(")", "").split(" ")[1:]

# ()바꾸기 " "로 split
replaced = replace_brackets(tds[2].text)
민간공고대수 = replace_brackets(tds[2].text) # 민간공고대수
접수대수 = replace_brackets(tds[3].text) # 접수대수
출고대수 = replace_brackets(tds[4].text) # 출고대수
출고잔여대수 = replace_brackets(tds[5].text) # 출고잔여대수

# 시도, 지역구분 추출
ths = tr.find_all("th")
sido = ths[0].text
region = ths[1].text
print(sido, region, 민간공고대수, 접수대수, 출고대수, 출고잔여대수)

# 데이터 구조 설계
# 우선순위, 법인과기관, 택시, 우선비대상
form = lambda a, b, c, d, e:{"시도":a, "지역":b, "구분1":c, "구분2":d, "대수":e}

서울_특별시 = [
    {"시도":"서울", "지역":"서울특별시", "구분1":"민간공고대수", "구분2":"우선순위", "대수":1650},
    {"시도":"서울", "지역":"서울특별시", "구분1":"민간공고대수", "구분2":"법인과기관", "대수": 2500}
]

l = [
    form(sido, region, "민간공고대수", "우선순위", int(민간공고대수[0])),
    form(sido, region, "민간공고대수", "법인과기관", int(민간공고대수[1])),
    form(sido, region, "민간공고대수", "택시", int(민간공고대수[2])),
    form(sido, region, "민간공고대수", "우선비대상", int(민간공고대수[3])),
]

for item in l:
    print(item)