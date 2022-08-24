import requests

url = "https://www.ev.or.kr/portal/localInfo"
data = requests.get(url)
print(data.text)

f = open("local_info.html", "w+", encoding="utf-8")
f.write(data.text)
f.close()
