# 可變引數(參數)
# P90-P91, P134-P135

def greet(*names):
    for name in names:
        print('Hello,', name)
greet('Messi', 'Neymar', 'Jordan', 'Othani')

tuple1 = ('Messi', 'Neymar', 'Jordan', 'Othani')
greet(tuple1)
greet(*tuple1)  # 加*才能取得所有元素一個一個傳給可變引數

str1 = 'Python'
greet(str1)
greet(*str1)    # 加*才能取得所有元素一個一個傳給可變引數


def stu(**data):
    for key, value in data.items():
        print("{} is {}".format(key, value))
stu(name="Tom", age="25", mobile="0934111222")

# 用字典的方式呼叫stu函式將字典放入函式中
dict1 = {"name":"Tom", "age":25, "mobile":"0934111222"}
stu(**dict1)
