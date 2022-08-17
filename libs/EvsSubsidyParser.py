from bs4 import BeautifulSoup
import pandas as pd

class EvGoKrSubsidyParser():
    bsobj = None

    def __init__(self, html_text):
        self.bsobj = BeautifulSoup(html_text, "html.parser")
        self.set_trs()

    def set_trs(self):
        table = self.bsobj.find("table", {"class":"table_02_2_1"})
        tbody = table.find("tbody")
        self.trs = tbody.find_all("tr")

    def parse(self):
        l = []
        for tr in self.trs:
            l += self.parse_tr(tr)

        self.result = l
        return l

    def parse_tr(self, tr):
        tds = tr.find_all("td")

        replace_brackets = lambda x: x.replace("(", "").replace(")", "").split(" ")[1:]
        form = lambda a, b, c, d, e: {"시도": a, "지역": b, "구분1": c, "구분2": d, "대수": e}

        # ()바꾸기 " "로 split
        replaced = replace_brackets(tds[2].text)
        민간공고대수 = replace_brackets(tds[2].text)  # 민간공고대수
        접수대수 = replace_brackets(tds[3].text)  # 접수대수
        출고대수 = replace_brackets(tds[4].text)  # 출고대수
        출고잔여대수 = replace_brackets(tds[5].text)  # 출고잔여대수

        # 시도, 지역구분 추출
        ths = tr.find_all("th")
        sido = ths[0].text
        region = ths[1].text
        l = [
            form(sido, region, "민간공고대수", "우선순위", int(민간공고대수[0])), form(sido, region, "민간공고대수", "법인과기관", int(민간공고대수[1])),
            form(sido, region, "민간공고대수", "택시", int(민간공고대수[2])),
            form(sido, region, "민간공고대수", "우선비대상", int(민간공고대수[3])),
            form(sido, region, "접수대수", "우선순위", int(접수대수[0])),
            form(sido, region, "접수대수", "법인과기관", int(접수대수[1])),
            form(sido, region, "접수대수", "택시", int(접수대수[2])),
            form(sido, region, "접수대수", "우선비대상", int(접수대수[3])),
            form(sido, region, "출고대수", "우선순위", int(출고대수[0])),
            form(sido, region, "출고대수", "법인과기관", int(출고대수[1])),
            form(sido, region, "출고대수", "택시", int(출고대수[2])),
            form(sido, region, "출고대수", "우선비대상", int(출고대수[3])),
            form(sido, region, "출고잔여대수", "우선순위", int(출고잔여대수[0])),
            form(sido, region, "출고잔여대수", "법인과기관", int(출고잔여대수[1])),
            form(sido, region, "출고잔여대수", "택시", int(출고잔여대수[2])),
            form(sido, region, "출고잔여대수", "우선비대상", int(출고잔여대수[3])),
        ]

        # result에 저장
        return l

    def save_to_excel(self, filename = "시도별_전기승용.xlsx"):
        pd.DataFrame(self.result).to_excel(filename)
        print(f"엑셀 저장이 완료 되었습니다. 파일명:{filename}")

if __name__ == "__main__":
    html_text = open("ev_or_kr_local_info.html").read()
    ev_parser = EvGoKrSubsidyParser(html_text = html_text)
    r = ev_parser.parse()

    for item in r:
        print(item)

    ev_parser.save_to_excel("시도별_전기승용.xlsx")




