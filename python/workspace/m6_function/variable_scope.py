# 變數範圍
# P93-P97
'''
x = 10
y = 11

def main():
    x = 20
    z = 100
    print(x)
    print(y)
    print(z)

main()
print(x)
print(y)
'''

'''
x = 10

def outer():
    x = 20
    def inner():
        x = 30
        print(x)
    inner()
    print(x)

outer()
print(x)
'''
'''
x = 10
y = 11

def main():
    x = 20
    print(x)
    global y # 把區域變數改成全域範圍取代外面的y
    y = 22
    print(y)

main()
print(x)
print(y)
'''
'''
x = 10

def outer():
    x = 20
    def inner():
        nonlocal x
        print(x)
        x = 30

    inner()
    print(x)
    
outer()
print(x)
'''

x = 10  # 因global x與inner內x=30對調

def outer():
    x = 20

    def inner():
        global x #指定區域變數為全域變數
        print(x)
        x = 30

    inner()
    print(x)

outer()
print(x)
