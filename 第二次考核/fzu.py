import re
import requests
import pandas as pd
from bs4 import BeautifulSoup

url="https://jwch.fzu.edu.cn/jxtz.htm"
url2="https://jwch.fzu.edu.cn"
url3="https://jwch.fzu.edu.cn/info/1040/13079.htm"

# 函数用于提取信息和附件
def extract_info_and_attachments ( url ) :
    resp = requests.get ( url, headers=headers )
    resp.encoding = "utf-8"
    page = BeautifulSoup ( resp.text, "html.parser" )

    content_div = page.find ( 'div', class_='v_news_content' )
    content_text = '\n'.join ( s.strip () for s in content_div.stripped_strings ) if content_div else ''
    formatted_text = ''.join ( content_text.splitlines () )

    attachments = []
    ul = page.find ( "ul", attrs={"style" : "list-style-type:none;"} )
    if ul :
        lis = ul.find_all ( "li" )
        for li in lis :
            attachment_name = li.find ( "a" ).text.strip ()
            span_with_dynamic_id = li.find ( "span", id=re.compile ( r"^nattach" ) )
            webnewsid = span_with_dynamic_id.get ( "id" )
            webnewsid = str ( webnewsid ).replace ( "nattach", '' )
            down_num_href = f"https://jwch.fzu.edu.cn/system/resource/code/news/click/clicktimes.jsp?wbnewsid={webnewsid}&owner=1744984858&type=wbnewsfile&randomid=nattach"
            response = requests.get ( down_num_href )
            # 检查请求是否成功
            # 解析 JSON 数据
            data = response.json ()
            down_num = data['wbshowtimes']

            down_url = url2 + li.find ( "a" ).get ( "href" ).strip ()
            attachments.append ( {
                'attachment_name' : attachment_name,
                'down_num' : down_num,
                'down_url' : down_url
            } )

    return formatted_text, attachments


# 准备数据的存储结构
data_for_excel = []

# 设置headers和url
headers = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0"
}
base_url = "https://jwch.fzu.edu.cn"
start_number = 183

# 获取链接，作者，日期和标题
for i in range ( start_number, start_number - 5, -1 ) :
    current_url = f"{base_url}/jxtz/{i}.htm"
    resp = requests.get ( current_url, headers=headers )
    resp.encoding = "utf-8"
    page = BeautifulSoup ( resp.text, "html.parser" )
    ul = page.find ( "ul", attrs={"class" : "list-gl"} )
    lis = ul.find_all ( "li" ) if ul else []

    for li in lis :
        href = li.find ( "a" ).get ( "href" )
        if 'jsp' not in href :
            href = base_url + href.replace ( "..", "" )
            text = li.text.strip ()
            parts = re.split ( r'【', text )
            date = parts[0].strip ()
            author = parts[1].replace ( "】", '' ).strip () if len ( parts ) > 1 else ''
            parts2=re.split(r'\n',author)
            author=parts2[0].strip()

            title = ''.join ( parts2[1 :] ).strip ()

            print(title)
            # 提取正文和附件信息
            formatted_text, attachments = extract_info_and_attachments ( href )

            if attachments :
                for attachment in attachments :
                    data_for_excel.append ( {
                        'href' : href,
                        'date' : date,
                        'author' : author,
                        'title' : title,
                        'formatted_text' : formatted_text,
                        'down_num' : attachment['down_num'],
                        'down_url' : attachment['down_url'],
                        'attachment_name' : attachment['attachment_name']
                    } )
            else :
                data_for_excel.append ( {
                    'href' : href,
                    'date' : date,
                    'author' : author,
                    'title' : title,
                    'formatted_text' : formatted_text,
                    'down_num' : '',
                    'down_url' : '',
                    'attachment_name' : ''
                } )
    resp.close ()

# 将数据转换为pandas DataFrame
df = pd.DataFrame ( data_for_excel )

# 将DataFrame存储为Excel文件
excel_path = 'output.xlsx'
df.to_excel ( excel_path, index=False )

print ( f"Data has been written to {excel_path}" )
