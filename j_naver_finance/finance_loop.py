import bs4
import requests
from finance_find import find_crawl


def list_crawl(pram1):
    list_url = "https://finance.naver.com{}".format(pram1)
    # print(list_url)
    data = find_crawl(list_url, "code")
    return data


# if __name__ == '__main__':
Url = "https://finance.naver.com/"
html_text = requests.get(Url).text
bs_obj = bs4.BeautifulSoup(html_text, "html.parser")
#bs_obj.select("div#container > div.aside > div.group_aside > div.aside_area.aside_popular > table")
pop_list = bs_obj.select("div.aside_area.aside_popular table >tbody > tr > th > a")
href_list = []
for item in pop_list:
    # print(item['href'])
    href_list.append(item['href'])
# print(href_list)



