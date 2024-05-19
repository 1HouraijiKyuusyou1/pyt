import requests
from bs4 import BeautifulSoup

#取得網站資料 ，將資料存到response
url="https://www.ptt.cc/bbs/NBA/index.html"
response=requests.get(url)

#將response的文字檔用BeautifulSoup解析成html，存至soup
soup=BeautifulSoup(response.text,"html.parser")

#尋找標題中，有div標籤的class 的r-ent內容
artical=soup.find_all("div",class_="r-ent")
#print(artical[0])

data_list=[]    #清單
#找到div標間中,class_是要取得內容的清單
for a in artical:
    data={}     #字典
    title=a.find("div",class_="title")
    if title and title.a:
        title=title.a.text
    else:
        title="N/A"
    #print(title)
    data["標題"]=title
    
    date=a.find("div",class_="date")
    if date:
        date=date.text
    else:
        date="N/A"
   # print(date)
    data["日期"]=date

    popularity=a.find("div",class_="nrec")
    if popularity and popularity.span:
        popularity=popularity.span.text     #div段落下,class_="nrec"下,span的文字檔
    else:
        popularity="N/A"
    #print(popularity)
    data["人氣"]=popularity
    
    data_list.append(data)  #把字典資料data加入data清單
print(data_list)

    #print(f"人氣:{popularity} ,標題:{title} , 日期:{date}")     #將人氣,標題,日期整合為一行

while True:
    # 讓使用者輸入日期
    search_date = input("請輸入日期 (格式：月份/日期，例如 03/27,前面有0要替換成空格)：")
    # 找出符合使用者輸入日期的文章
    for data in data_list:
        if data["日期"] == search_date:
            print(f"日期:{data['日期']}，標題：{data['標題']}，人氣：{data['人氣']}")

    continue_search= input('是否繼續搜尋？(y/n)：')
    if continue_search.lower() != 'y':
        break
while True:
    search_keyword = input("請輸入關鍵字：")
    for data in data_list:
        if search_keyword.lower() in data["標題"].lower():
            print(f"日期:{data['日期']}，標題：{data['標題']}，人氣：{data['人氣']}")

    continue_search = input('是否繼續搜尋？(y/n)：')
    if continue_search.lower() != 'y':
        break 