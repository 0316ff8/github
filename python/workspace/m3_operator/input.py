'''
s = input('Please input a string: ')
print(s)

n = int(input('Please input a number: '))
print(n + 3)

n = eval(input('Please input a number: '))
print(n + 3)

n1, n2 = eval(input('Please input a number: '))
print(n1, n2)
'''
s1, s2 = eval(input('Please input a string: '))
print(s1, s2) # 不能用int, 只能用eval, 輸入單引號與雙引號都可以, 如: "aa", "bb"
