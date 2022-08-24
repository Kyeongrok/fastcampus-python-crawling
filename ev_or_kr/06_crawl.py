import requests
from libs.evparser import EvGoKrSubsidyParser

url = "https://www.ev.or.kr/portal/localInfo"
data = requests.get(url)

ev_parser = EvGoKrSubsidyParser(data.text)
ev_parser.save_to_excel("crawl_subsidy_all.xlsx")
# ev_parser.parse()
