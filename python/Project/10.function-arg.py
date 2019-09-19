# 參數的預設資料
# def 函式名稱(參數名稱=預設資料):
#     函式內部的程式碼

# 範例
# 參數msg預設資料為"Hello"
# def say(msg="Hello"):
#     print(msg)

# say("Hello Function")   #印出Hello Function
# say()                   #印出預設資料Hello

# 範例1
# def power(base,exp):
#     print(base**exp)
# power(3,2)    #結果為9

# 範例2
# def power(base,exp=0):
#     print(base**exp)
# power(3,2)    #結果為9
# power(4)      #沒給exp會用預設資料exp=0來帶，4的0次方為1

#-----------------------------------------------------------
# 使用參數名稱對應
# def 函式名稱(名稱1,名稱2):
#     函式內部的程式碼
# 呼叫函式，以參數名稱對應資料
# 函式名稱(名稱2=3,名稱1=5)

# 範例
# 定義一個可以做加法的函式
# def divide(n1,n2):
#     result=n1/n2
#     print(result)
# divide(2,4)         #印出0.5
# divide(n2=2,n1=4)   #印出2.0

# 範例1
# def divide(n1,n2):
#     print(n1/n2)
# divide(2,4)         #印出0.5
# divide(n2=2,n1=4)   #印出2.0

#-----------------------------------------------------------
# 無限/不限 參數資料
# def 函式名稱(*無限參數):
#     無限參數以Tuple資料型態處理
#     函式內部的程式碼
# 呼叫函式，可傳入無限數量的參數
# 函式名稱(資料一,資料二,資料三)

# 範例
# 函式接受無限參數msgs
# def say(*msgs):
#     #以Tuple列表的方式處理
#     for msg in msgs:
#         print(msg)
# 呼叫函式，傳入三個參數資料
# say("Hello","Arbitrary","Arguments")


# 範例1
def avg(*ns):
    sum=0
    for n in ns:
        sum=sum+n
    print(sum/len(ns))  #總和/ns列表的長度
avg(3,4)                #(3+4)/2，印出3.5
avg(3,5,10)             #(3+5+10)/3，印出6.0
avg(1,4,-1,-8)          #(1+4+(-1)+(-8))/4，印出-1.0