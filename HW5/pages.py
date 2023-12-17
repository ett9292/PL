from bs4 import BeautifulSoup #匯入BS套件
import urllib.request as req #匯入urllib 套件

file=open("IThelp_pages.txt",mode="w",encoding="utf-8") #開啟一個文檔
url="https://ithelp.ithome.com.tw" #設置要爬蟲的第一頁

def getContent(url):
    #讓網頁覺得我們是正常瀏覽器，所以附加Request Headers
    request=req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    })

    with req.urlopen(request) as response:
        data=response.read().decode("utf-8") #中文編碼

    #解析原始碼，取的每篇文章的標題以及內文連結
    root=BeautifulSoup(data, "html.parser")
    titles=root.find_all("h3",class_="qa-list__title") #尋找class="qa-list__title"的h3標籤
    for title in titles:
        if title.a != None: #如果標題包含a標籤(沒有被刪除)，印出來
            file.write("<<" + title.a.string + ">>" + "\n") #寫入標題
            
            ct = title.a["href"] #抓取每則文章的超連結
            request2=req.Request(ct,headers={
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
            })
            with req.urlopen(request2) as response:
                contents=response.read().decode("utf-8") #中文編碼
            
            content = BeautifulSoup(contents, "html.parser").find("div", class_ = "markdown__style") #找出內文
            file.write(content.text + "\n")

    
    nextLink=root.find("a",string="下一頁") #找到下頁標籤
    return nextLink["href"]

count = 0 #設定翻頁
while count<100: #抓取100頁
    file.write("-------------------------------------第" + str(count+1) + "頁-------------------------------------" + "\n")
    #進行翻頁
    url = getContent(url)
    count += 1

file.close()