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
driver.get(url=Url)
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/div[1]/div[1]/div/div/div/a').send_keys(Keys.ENTER)
time.sleep(3)
image_url = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/div/picture/img").get_attribute('src')
# 안되는 이유 설명
# request.urlretrieve(image.get_attribute('src'), "image01.jpg")
req = Request(image_url, headers={'User-Agent': 'Mozilla/5.0'})
f = open("text.jpg", 'wb')
f.write(urlopen(req).read())
f.close()
print(image_url)


