# 載入模組
# import urllib.request

# 下載特定網址資料
# import urllib.request as request
# with request.urlopen(網址) as response:
#     data=response.read()
# print(data)

# 尋找公開資料，選擇適合的資料來源，如:台北市政府公開資料，確認資料格式 JSON、CSV或其他格式
# 解讀JSON格式，使用內建的JSON模組


# 網路連線
# import urllib.request as request
# src="https://www.ntu.edu.tw/"
# with request.urlopen(src) as response:
#     data=response.read().decode("utf-8")    # 取得台灣大學網站的原始碼(HTML、CSS、JS)
#                                             # .decode("utf-8") 網頁編碼轉換為utf-8
# print(data)


# 串接、擷取公開資料
import urllib.request as request
import json
src="https://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=296acfa2-5d93-4706-ad58-e83cc951863c"
with request.urlopen(src) as response:
    data=json.load(response)    #利用JSON模組處理JSON資料格式
# 將公司名稱列表出來
# clist=data["result"]["results"]
# for company in clist:
#     print(company["公司名稱"])
# 將公司名稱列表存到檔案
clist=data["result"]["results"]
with open("company.txt",mode="w",encoding="utf-8") as file:
    for company in clist:
        file.write(company["公司名稱"]+"\n")