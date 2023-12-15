import requests
from bs4 import BeautifulSoup
import sqlite3

# 创建或连接到SQLite数据库
conn = sqlite3.connect('history_today.db')
cursor = conn.cursor()

# 创建历史今天的数据表
cursor.execute('''
CREATE TABLE IF NOT EXISTS history_today (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    year TEXT,
    event_type TEXT,
    title TEXT,
    content TEXT
)
''')

# 设置百度百科历史上的今天的URL
url = 'https://baike.baidu.com/calendar/'

# 发送HTTP请求获取页面内容
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

# 查找历史上的今天的事件
events = soup.find_all(class_='calendar-content')

for event in events:
    year = event.find(class_='calendar-year').text.strip()
    event_type = event.find(class_='calendar-type').text.strip()
    title = event.find(class_='calendar-title').text.strip()
    content = event.find(class_='calendar-content-detail').text.strip()

    # 插入数据到数据库中
    cursor.execute('''
    INSERT INTO history_today (year, event_type, title, content)
    VALUES (?, ?, ?, ?)
    ''', (year, event_type, title, content))

# 提交事务并关闭数据库连接
conn.commit()
conn.close()