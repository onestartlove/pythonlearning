import re
import requests
from bs4 import BeautifulSoup

url = "https://jwch.fzu.edu.cn/jxtz.htm"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
page_info = soup.find("div", class_="page-info")
if page_info is not None:
    page_text = page_info.text.strip()
    total = int(re.search(r"共(\d+)条", page_text).group(1))
else:
    total = 0

import pymysql

db = pymysql.connect(host="localhost", user="root", password="123456", database="test", charset="utf8mb4")
cursor = db.cursor()

url = "https://jwch.fzu.edu.cn/jxtz.htm"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
table = soup.find("table", class_="table table-bordered")
trs = table.find_all("tr")[1:]
for tr in trs:
    tds = tr.find_all("td")
    notice = {}
    notice["title"] = tds[1].a.text.strip().replace("\r\n", "")
    notice["date"] = tds[2].text.strip().replace("\r\n", "")
    notice["source"] = tds[3].text.strip().replace("\r\n", "")
    notice["link"] = tds[1].a["href"]
    # 存入数据库
    sql = "INSERT INTO notices(title, date, source, link) VALUES(%s, %s, %s, %s)"
    cursor.execute(sql, (notice["title"], notice["date"], notice["source"], notice["link"]))
db.commit()
db.close()
