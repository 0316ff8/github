#判斷式

#if True:
#    print("True 執行")
#else:
#    print("False 執行")

#x=input("請輸入數字: ") #取得字串型式的使用者輸入
#x=int(x)    #將字串型態轉換成數字型態
#if x>200:
#    print("大於 200")
#elif x>100:
#    print("大於 100，小於等於 200")
#else:
#    print("小於等於 100")

#基本加法運算
#n1=int(input("請輸入第一組數字: "))
#n2=int(input("請輸入第一組數字: "))
#print(n1+n2)

#四則運算
n1=float(input("請輸入第一組數字: "))
n2=float(input("請輸入第一組數字: "))
op=input("請輸入運算: +,-,*,/: ")
#== 是比較運算：比較資料是否相同，回傳布林值
#= 是指定運算：把資料放進變數中
if op=="+":
    print(n1+n2)
elif op=="-":
    print(n1-n2)
elif op=="*":
    print(n1*n2)
elif op=="/":
    print(n1/n2)
else:
    print("不支援的運算")    