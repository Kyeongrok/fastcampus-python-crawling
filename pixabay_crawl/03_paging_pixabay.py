import os

from selenium import webdriver
import chromedriver_autoinstaller
from time import sleep

from urllib.request import Request, urlopen


from selenium.webdriver.common.by import By

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
driver.implicitly_wait(5)


def crawl_image(keyword, pages):
    image_urls = []
    for i in range(1, pages + 1):
        url = f"https://pixabay.com/ko/images/search/{keyword}/?pagi={i}"
        driver.get(url=url)

        # find(), find_all() .find_elements
        image_area_xpath = "/html/body/div[1]/div[2]/div/div[3]/div/div[3]"
        image_area = driver.find_element(By.XPATH, image_area_xpath)
        image_elements = image_area.find_elements(By.TAG_NAME, "img")

        for image_element in image_elements:
            image_url = ""
            if image_element.get_attribute("data-lazy") is None:
                image_url = image_element.get_attribute("src")
            else:
                image_url = image_element.get_attribute("data-lazy")
            print(image_url)
            image_urls.append(image_url)

    return image_urls



def crawl_and_save_image(keyword, pages):

    path = keyword
    image_urls = crawl_image(keyword, pages)
    print(len(image_urls))

    # 디렉토리 만들기
    if not os.path.exists(path):
        os.mkdir(path)

    for i in range(len(image_urls)):
        image_url = image_urls[i]
        image_byte = Request(image_url, headers={'User-Agent': 'Mozilla/5.0'})
        filename = image_url.split("/")[-1]
        f = open(f"{path}/{filename}", "wb")
        f.write(urlopen(image_byte).read())
        f.close()


crawl_and_save_image("가지", 1)
crawl_and_save_image("양파", 2)
