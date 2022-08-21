import bs4
import requests


# find, select 사용법

def find_crawl(url, cod):
    html_text = requests.get(url).text
    bs_obj = bs4.BeautifulSoup(html_text, "html.parser")
    if cod == "code":
        price = bs_obj.find("p", {"class": "no_today"}).find("span", {"class": "blind"}).text
        obj_code = bs_obj.find("div", {"class": "description"}).find("span", {"class": "code"}).text
        name = bs_obj.select("div.wrap_company > h2 > a")[0].get_text()
        obj_list = [name, obj_code, price]
        return obj_list
    elif cod == "kos":
        kos_table = bs_obj.select("div.section_search > table > tbody > tr > td > a")
        for item in kos_table:
            print(item.text)
        return kos_table


if __name__ == '__main__':
    Url1 = "https://finance.naver.com/item/main.naver?code=005930"
    Url2 = "https://finance.naver.com/search/searchList.naver?query=%C4%DA%BD%BA%C7%C7"
    Url3 = "https://finance.naver.com/search/searchList.naver?query=%C4%DA%BD%BA%B4%DA"
    print(find_crawl(Url1, "code"))
    print(find_crawl(Url3, "kos"))
