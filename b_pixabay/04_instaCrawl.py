from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import chromedriver_autoinstaller

insta_id = ""
insta_pw = ""
search = "고양이"

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
driver.implicitly_wait(3)# element를 모두 로드할 때 까지 기다려줘야함
Url = "https://www.instagram.com/"
driver.get(url=Url)
# 인스타 로그인
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(insta_id)
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(insta_pw)
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div').send_keys(Keys.ENTER)
#  /html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div
driver.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(search)
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]')\
    .click()
time.sleep(10)
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a').click()
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div/button').click()
# img = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[1]/div/div[1]/div[2]/div/div/div/ul/li[2]/div/div/div/div/div[1]/img').get_attribute("secret")
# print(img)
time.sleep(1000)
