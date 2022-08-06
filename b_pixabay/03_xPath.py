from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import chromedriver_autoinstaller

insta_id = "01028351203"
insta_pw = "gkawjdgh98!"

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
driver.implicitly_wait(5) # element를 모두 로드할 때 까지 기다려줘야함
Url = "https://www.instagram.com/"
driver.get(url=Url)
# 그냥 인스타 로그인
# driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(insta_id)
# driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(insta_pw)
# driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()
# 페북으로 로그인
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[5]/button').click()
driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(insta_id)
driver.find_element(By.XPATH, '//*[@id="pass"]').send_keys(insta_pw)
driver.find_element(By.XPATH, '//*[@id="loginbutton"]').click()
time.sleep(100)


