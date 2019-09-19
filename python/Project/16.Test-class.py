# 類別的定義與使用
# 封裝的變數或函式，統稱類別的屬性
# 要先定義(建立)類別，然後才能使用類別中封裝的屬性

# 定異類別基本語法
# class 類別名稱(第一字不用數字，使用大寫):
#   定義封裝的變數
#   定義封裝的函式

# 程式範例
# 定義Test類別
# class Test:
#     x=3 # 定義變數
#     def say(): # 定義函式
#         print("Hello")

# 使用類別基本語法
# 類別名稱.屬性名稱

# 程式範例
# 定義Test類別
# class Test:
#     x=3 
#     def say():
#         print("Hello")
# 使用Test類別
# Test.x+3 # 取得屬性x的資料3
# Test.say() # 呼叫屬性say函式

# 定義類別、與類別屬性(封裝在類別中的變數與函式)
# 定義一個類別IO，有兩個屬性 supportedSrcs和read
# 範例一
# class IO:
#     supportedSrcs=["console","file"]
#     def read(src):
#         print("Read from",src)
# 使用類別
# print(IO.supportedSrcs)
# IO.read("file")

# 範例二
class IO:
    supportedSrcs=["console","file"]
    def read(src):
        if src not in IO.supportedSrcs:
            print("Not Supported")
        else:
            print("Read from",src)

print(IO.supportedSrcs)
IO.read("file")
IO.read("internet")

