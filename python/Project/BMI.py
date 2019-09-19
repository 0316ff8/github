#問題：輸入身高跟體重計算BMI值並判斷過胖或過瘦
#身高：height
#體重：weight
#身高體重指數：BMI
#BMI = 體重 (公斤) / (身高 (公尺) x 身高 (公尺))

h=float(input("請輸入您的身高(cm): "))
h=h/100 #換算成公尺
w=float(input("請輸入您的體重(kg): "))
BMI=w/(h*h)
#round(x,n) 方法返回 x 的小數點四舍五入到n個數字
if BMI>24:
    print("BMI為"+str(round(BMI,2))+" 死胖子!")
elif BMI<=24 and BMI>=18.5:
    print("BMI為"+str(round(BMI,2))+" 沒想到你人模人樣啊!")
else:
    print("BMI為"+str(round(BMI,2))+" 你真瘦!")
