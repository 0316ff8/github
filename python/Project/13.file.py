# 開啟檔案
# 檔案物件=open(檔案路徑,mode=開啟模式)

# 讀取模式: r
# 寫入模式: w
# 讀寫模式: r+
#---------------------------------------------------------------
# 關閉檔案(釋放資源)
# 檔案物件.close()
#---------------------------------------------------------------
# 儲存(寫入)檔案

# 寫入文字
# 檔案物件.write(字串)
# file=open("data.txt",mode="w")  #開啟
# file.write("Hello File")    #操作(讀取或寫入)
# file.close()    #關閉

# 寫入換行符號
# 檔案物件.write("這是範例文字\n")
# file=open("data.txt",mode="w")  #開啟
# file.write("Hello File\nSecond Line")    #操作
# file.close()    #關閉

# 顯示中文會有亂碼，須新增【encoding="utf-8"】才會正常顯示
# file=open("data.txt",mode="w",encoding="utf-8")  #開啟
# file.write("球神梅西\n帽子戲法")    #操作
# file.close()    #關閉

# 最佳實務
# with open(檔案路徑,mode=開啟模式) as 檔案物件:
#     讀取或寫入檔案的程式
# 以上區塊會自動、安全的關閉檔案

# 最佳化寫法
# 範例1(對應下方讀取的範例1)
# with open("data.txt",mode="w",encoding="utf-8") as file:
#     file.write("球神梅西\n帽子戲法")

# 範例2(對應下方讀取的範例2)
# with open("data.txt",mode="w",encoding="utf-8") as file:
#     file.write("5\n3")
#---------------------------------------------------------------
# 讀取檔案

# 檔案物件.read()

# 一次讀取一行
# for 變數 in 檔案物件:
#     從檔案依序讀取每行文字到變數中

# 範例1
# with open("data.txt",mode="r",encoding="utf-8") as file:
#     data=file.read()
# print(data)

# 範例2
# 把檔案中的數字資料，一行一行的讀取出來，並計算總合
# sum=0
# with open("data.txt",mode="r",encoding="utf-8") as file:
#     for line in file:   #一行一行讀取
#         sum+=int(line)
# print(sum)

# 使用JSON格式讀取、複寫檔案
# 讀取 JSON 格式
# import json
# 讀取到的資料=json.load(檔案物件)
# 寫入JSON格式
# import json
# json.dump(要寫入的資料,檔案物件)

# 範例1
# import json
# with open("config.json",mode="r") as file:
#     data=json.load(file)
# print(data) #data是一個字典資料
# print("name: ",data["name"])
# print("version: ",data["version"])

# 範例2
# 從檔案中讀取JSON資料，放入變數data裡面
import json
with open("config.json",mode="r") as file:
    data=json.load(file)
print(data) #data是一個字典資料
data["name"]="New Name" #修改變數中的資料
# 把最新的資料更新回檔案中
with open("config.json",mode="w") as file:
    json.dump(data,file)

