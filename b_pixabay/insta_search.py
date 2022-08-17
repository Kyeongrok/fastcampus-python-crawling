from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import chromedriver_autoinstaller
from bs4 import BeautifulSoup

insta_id = ""
insta_pw = ""
search = "고양이"

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
driver.implicitly_wait(3)  # element를 모두 로드할 때 까지 기다려줘야함
Url = "https://www.instagram.com/"
driver.get(url=Url)


def insta_login(id, pw):
    driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(id)
    driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(pw)
    driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').send_keys(Keys.ENTER)


def insta_search(q):
    insta_login(insta_id, insta_pw)
    driver.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(q)
    time.sleep(3)
    driver.find_element(By.XPATH,
                        '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]') \
        .click()
    time.sleep(10)
    driver.find_element(By.XPATH,
                        '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a').click()
    driver.find_element(By.XPATH,
                        '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div/button').click()
    like_comment('너무 귀엽네요')
    time.sleep(1000)


def like_comment(ms):
    next_button = '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div/button'
    like = '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button'
    send = '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/button'
    text_input = '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea'
    comment_block = '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/div[3]/div'
    for i in range(0, 7):
        try:
            driver.find_element(By.XPATH, like).click()
            driver.find_element(By.XPATH, text_input).click()
            driver.find_element(By.XPATH, text_input).send_keys(ms)
            driver.find_element(By.XPATH, send).click()
            driver.find_element(By.XPATH, next_button).click()
        except Exception as e:
            print(e)
            driver.find_element(By.XPATH, next_button).click()


# img = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[1]/div/div[1]/div[2]/div/div/div/ul/li[2]/div/div/div/div/div[1]/img').get_attribute("secret")
# print(img)


if __name__ == '__main__':
    insta_search(search)
    driver.close()
