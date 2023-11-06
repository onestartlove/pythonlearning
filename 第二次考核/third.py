import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
# 读取工作簿
df = pd.read_excel('output.xlsx', engine='openpyxl')
print(df.head(5))


import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"]=["SimHei"] #设置字体
plt.rcParams["axes.unicode_minus"]=False


df['author'] = df['author'].str.replace('_x000D_\n', '', regex=False)

# 处理缺失值
df['down_num'].fillna(0, inplace=True)  # 假设没有下载次数的可以用0替换

# 转换日期为 pandas datetime
df['date'] = pd.to_datetime(df['date'])

author_downloads = df.groupby('author')['down_num'].sum().sort_values(ascending=False)

print(author_downloads)

author_downloads_filtered = author_downloads[author_downloads > 0]
plt.figure(figsize=(10, 8))  # 可以调整图形大小
author_downloads_filtered.plot(kind='bar')
plt.title('Total Download Numbers by Author')
plt.xlabel('Author')
plt.ylabel('Download Numbers')
plt.xticks(rotation=45)  # 旋转X轴的标签
plt.tight_layout()  # 自动调整子图参数，使之填充整个图像区域
plt.show()

# 每天的通知数分析
daily_notices = df['date'].value_counts().sort_index()

# 打印每天的通知数量
print(daily_notices)

# 绘制每天通知数量的时间序列图
daily_notices.plot(kind='line')
plt.title('Number of Notices per Day')
plt.xlabel('Date')
plt.ylabel('Number of Notices')
plt.show()

# 通过绘制滚动平均值找出通知较为密集的时间段
daily_notices.rolling(window=7).mean().plot(kind='line')  # 7天滚动平均
plt.title('7-Day Rolling Average of Notices per Day')
plt.xlabel('Date')
plt.ylabel('Average Number of Notices')
plt.show()
