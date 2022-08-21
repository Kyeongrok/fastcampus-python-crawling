import requests
from bs4 import BeautifulSoup


def crawl(code):
    url = f"https://finance.naver.com/item/main.naver?code={code}"
    res = requests.get(url)
    bsobj = BeautifulSoup(res.text, "html.parser")

    div_today = bsobj.find("div", {"class":"today"})
    em = div_today.find("em")

    price = em.find("span", {"class":"blind"}).text
    h_company = bsobj.find("div", {"class":"h_company"})
    name = h_company.a.text
    div_description = h_company.find("div", {"class":"description"})
    code = div_description.span.text

    table_no_info = bsobj.find("table", {"class":"no_info"})
    tds = table_no_info.tr.find_all("td")
    volume = tds[2].find("span", {"class":"blind"}).text

    dic = {"price":price, "name":name, "code":code, "volume":volume}
    return dic

dic = crawl("035720")
print(dic)




