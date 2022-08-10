from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.implicitly_wait(3)# element를 모두 로드할 때 까지 기다려줘야함
Url = "https://pixabay.com/ko/"
driver.get(url=Url)
