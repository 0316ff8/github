#定義函式
#函式內部的程式碼，若是沒有做《函式呼叫》，就不會執行

#def 函式名稱(參數名稱):
#    函式內部的程式碼

# 定義一個印出Hello的函式
# def sayHello():
#     print("Hello")

# 定義可以印出任何訊息的函式
# def say(msg):
#     print(msg)

# 定義一個可以做加法的函式
# def add(n1,n2):
#     result=n1+n2
#     print(result)

#-------------------------------------------------------
#呼叫函式

# 定義一個印出Hello的函式
# def sayHello():
#     print("Hello")
# 呼叫上方定義的函式
# sayHello()

# 定義可以印出任何訊息的函式
# def say(msg):
#     print(msg)
# 呼叫上方定義的函式
# say("Hello Function")
# say("Hello Python")

# 定義一個可以做加法的函式
# def add(n1,n2):
#     result=n1+n2
#     print(result)
# 呼叫上方定義的函式
# add(3,4)
# add(7,8)

#-------------------------------------------------------
#回傳值

#def 函式名稱(參數名稱):
#   函式內部的程式碼
#   return  #結束函式，回傳None
#   或者
#   return 資料 #結束函式，回傳《資料》

#函式回傳None
#def say(msg):
#    print(msg)
#    return
# 呼叫函式，取得回傳值
#value=say("Hello Function")
#print(value)    
#印出Hello Function跟None

# 函式回傳字串 Hello
# def add(n1,n2):
#     result=n1+n2
#     return "Hello"
# 呼叫函式，取得回傳值
# value=add(3,4)
# print(value)    #印出Hello

# 函式回傳 n1+n2 的結果
# def add(n1,n2):
#     result=n1+n2
#     return result
# 呼叫函式，取得回傳值
# value=add(3,4)
# print(value)    #印出7


#範例1:
#def multiply(n1,n2):
#    print(n1*n2)
# multiply(3,4)
# multiply(10,8)
# 印出12跟80

#範例2:
#def multiply(n1,n2):
#    print(n1*n2)
#value=multiply(3,4)
#print(value)
#印出12跟None

#範例3:
#def multiply(n1,n2):
#    print(n1*n2)
#    return n1*n2
#value=multiply(3,4)
#print(value)
#印出12跟12

#範例4:
#def multiply(n1,n2):
#    return n1*n2
#value=multiply(3,4)+multiply(10,5) #(3*4)+(10*5)
#print(value)

#---------------------------------------------------------
#程式的包裝

#範例1
# def calculate():
#     sum=0
#     for n in range(1,11):
#         sum=sum+n
#     print(sum)

# calculate() #印出55
# calculate() #印出55，可以做多次的呼叫

#函式可以用來做程式的包裝: 同樣的邏輯可以重複利用

#範例2
def calculate(max):
    sum=0
    for n in range(1,max+1):
        sum=sum+n
    print(sum)

calculate(10)
calculate(20)