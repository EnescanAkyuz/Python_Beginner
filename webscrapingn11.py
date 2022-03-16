import requests
from bs4 import BeautifulSoup

url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"
html = requests.get(url).content

soup = BeautifulSoup(html, "html.parser")

list = soup.find("section",{"class":"ems-prd-list"}).find_all("li",{"class":"column"},limit=5)

for li in list:
    title = li.div.a.h3.text.strip()
    print(title)

# print(list)

