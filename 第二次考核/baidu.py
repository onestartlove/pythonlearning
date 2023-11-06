import pandas as pd
import brotli
import requests

# 请求URL
url = 'https://baike.baidu.com/cms/home/eventsOnHistory/11.json'
records = []

# 请求头信息
headers = {
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Connection': 'keep-alive',
    'Host': 'baike.baidu.com',
    'Referer': 'https://baike.baidu.com/calendar',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0',
    'X-Requested-With': 'XMLHttpRequest'
}


for i in range(1,13):
    month = f"{i:02d}"
    url=f'https://baike.baidu.com/cms/home/eventsOnHistory/{month}.json'
    response = requests.get(url, headers=headers)

    # 检查内容是否使用了 Brotli 编码
    if response.headers.get('Content-Encoding') == 'br':
        # 解压缩 Brotli 编码的内容
        decompressed_data = brotli.decompress(response.content)
        # 将解压缩的数据解码为字符串
        content = decompressed_data.decode('utf-8')
    else:
        # 如果内容没有使用 Brotli 编码，直接解码响应内容
        content = response.text


    import json
    data = json.loads(content)
    # 提取我们需要的信息
    for month, days in data.items():
        for day, events in days.items():
            for event in events:
                record = {
                    'year': event['year'],
                    'type': event['type'],
                    'title': event['title'],
                    'desc': event['desc']
                }
                records.append(record)

# 创建 DataFrame
df = pd.DataFrame(records)
df.to_excel('events.xlsx', index=False)

