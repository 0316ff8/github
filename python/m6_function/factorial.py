# 撰寫一函式名為factorial, 傳一整數參數, 並傳回此整數的階層值
# P86
def factorial(num):
    result = 1
    for n in range(num, 1, -1):
       result *=n
    return result

def main():
    num=eval(input('number:'))
    print('{}!={}'.format(num, factorial(num)))

main()
