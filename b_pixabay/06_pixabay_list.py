import sys
import urllib.request
from urllib.request import Request, urlopen

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import chromedriver_autoinstaller
import os
from urllib import request
chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.implicitly_wait(3)# element를 모두 로드할 때 까지 기다려줘야함
Url = "https://pixabay.com/ko/"
driver.get(Url)
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="hero"]/div[4]/form/div/span/input').send_keys('강아지')
driver.find_element(By.XPATH, '//*[@id="hero"]/div[4]/form/div/input').click()
time.sleep(3)
image_area = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div')
images = image_area.find_elements(By.TAG_NAME, "img")
path = 'crawl_img'
try:
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        print('이미 폴더가 존재 합니다.')
        sys.exit(0)
except OSError:
    print(OSError)
    sys.exit(0)
image_list = []
for image in images:
    if image.get_attribute('data-lazy-src') is None:
        image_list.append(image.get_attribute('src'))
    else:
        image_list.append(image.get_attribute('data-lazy-src'))
for img in image_list:
    req = urllib.request.Request(img, headers={'User-Agent': 'Mozila/5.0'})
    filename = img.split('/')[-1]
    savePath = path+'/'+filename
    f = open(savePath, 'wb')
    f.write(urllib.request.urlopen(req).read())
    f.close()


print(image_list)
time.sleep(100)
