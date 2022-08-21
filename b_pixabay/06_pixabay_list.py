import sys
import urllib.request

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import chromedriver_autoinstaller
import os
import uuid
chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.implicitly_wait(5)# element를 모두 로드할 때 까지 기다려줘야함

def collect_image_url(keyword, n, path='crawl_img'):
    # path = path + uuid.uuid1(uuid1).__str__()

    image_list = []
    for i in range(1, n + 1):
        url = f'https://pixabay.com/ko/images/search/{keyword}/?pagi={i}'
        driver.get(url)
        time.sleep(2)
        image_area_xpath = "/html/body/div[1]/div[2]/div/div[3]/div/div[3]"
        image_area = driver.find_element(By.XPATH, image_area_xpath)
        images = image_area.find_elements(By.TAG_NAME, "img")


        for image in images:
            if image.get_attribute('data-lazy') is None:
                image_list.append(image.get_attribute('src'))
                print(image.get_attribute('src'))
            else:
                image_list.append(image.get_attribute('data-lazy'))
                print(image.get_attribute('data-lazy'))


        time.sleep(3)
        # next_button_xpath = "/html/body/div[1]/div[2]/div/a"
        # driver.find_element(By.XPATH, next_button_xpath).click()


    # 디렉토리 만들기
    try:
        if not os.path.exists(path):
            os.mkdir(path)
        else:
            print('이미 폴더가 존재 합니다.')
            sys.exit(0)
    except OSError:
        print(OSError)
        sys.exit(0)

    for img in image_list:
        req = urllib.request.Request(img, headers={'User-Agent': 'Mozilla/5.0'})
        filename = img.split('/')[-1]
        savePath = path+'/'+filename
        f = open(savePath, 'wb')
        f.write(urllib.request.urlopen(req).read())
        f.close()


collect_image_url("사과", 2, "crawl_img2")
print('크롤 완료')
