# selenium으로 자동화 프로그램을 만들 때, 현재 설치된 Chrome 등의 브라우저 버전에 맞는
# 드라이버를 다운로드 받고 그 드라이버를 로딩할 수 있도록 path를 변경해야 합니다.
# 만약 Chrome을 업데이트하게 되면, 업데이트된 버전에 맞는 Chrome driver를 다시 받아야 합니다.
# 이런 작업은 매우 귀찮고 번거롭습니다.
# 1. 그냥 하는 경우
# https://chromedriver.storage.googleapis.com/index.html?path=94.0.4606.41/
# 2. 크롬 오토 인스톨러를 다운 받는다
#  ssl 에서 나는 경우: https://www.codeit.kr/community/threads/19775
import time

from selenium import webdriver
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

# driver = webdriver.Chrome(executable_path="../webdriver/chromedriver")
driver = webdriver.Chrome()
Url = "https://www.instagram.com/explore/tags/%EC%95%84%EC%9D%B4%EC%9C%A0/"
driver.get(url=Url)
time.sleep(100)
pageString = driver.page_source
print(pageString)

# driver.close()
