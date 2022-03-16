import requests
from bs4 import BeautifulSoup

url = "https://www.monsternotebook.com.tr/laptop/?srt=UP"

html = requests.get(url).content

soup = BeautifulSoup(html,"html.parser")

list = soup.find_all("li",{"class":"ems-prd"}, limit=5)

# print(list)

for li in list:
    name = li.div.a.get("href").strip("/")
    print(name)