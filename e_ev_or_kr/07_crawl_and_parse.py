import requests
from libs.EvsSubsidyParser import EvGoKrSubsidyParser

print("데이터 수집을 시작 합니다.")
data = requests.get("https://www.ev.or.kr/portal/localInfo")
print("데이터 수집이 완료 되었습니다. 파싱을 시작 합니다.")

ev_parser = EvGoKrSubsidyParser(data.text)
l = ev_parser.parse()
ev_parser.save_to_excel("시도별_전기승용2.xlsx")
