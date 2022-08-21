from selenium import webdriver
import chromedriver_autoinstaller
import time
import os

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.implicitly_wait(3)

url = "https://www.instagram.com/"
driver.get(url=url)

def login(id, password):
    input_id = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
    input_id.send_keys(id)
    driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
    # driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]').click()
    driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').send_keys(Keys.ENTER)

def search(hashtag, scroll_times):
    url = f"https://www.instagram.com/explore/tags/{hashtag}/"
    driver.get(url=url)
    time.sleep(6)
    # print(driver.page_source)

    for _ in range(scroll_times):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

id = os.getenv("INSTA_ID")
password = os.getenv("INSTA_PW")

login(id, password)
time.sleep(5)
search(hashtag="강아지", scroll_times=2)

time.sleep(100)
