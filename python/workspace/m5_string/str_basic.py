str1 = 'Python'
print('y' in str1)
print('py' in str1)
for i in str1:
    print(i, end=' ')
print()

print('-----------------------------')

# 索引運算子
print(str1[2])
print(str1[-1])

print('-----------------------------')

# 分割運算子
print(str1[1:4])
print(str1[:4])
print(str1[:-2])
print(str1[1:])
print(str1[-4:])
print(str1[1:-1])

print('-----------------------------')

print(len(str1))
print(max(str1))
print(min(str1))
print(str1 * 3)
