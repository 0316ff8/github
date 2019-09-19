# 判斷字串開頭
s = 'Hello world, welcome to Python world.'
print(s.startswith('Hello'))
print(s.startswith('hello'))

# 判斷字串結尾
s1 = 'hello.py'
print(s1.endswith('.py'))

print('-----------------------------')
# find由左開始找到第一個字的索引位置, rfind若有重複會找尾巴的索引位置
s = 'Hello world, welcome to Python world.'
print(s.find('world'))
print(s.find('World'))
print(s.rfind('world'))


print('-----------------------------')
s2 = 'Hello world, welcome to Python world. Hello world, welcome to Python world.'
index = s2.find('world')
print(s2.find('World', index + 1))
print(s2.count('world'))

print('-----------------------------')
s2 = 'Hello world, welcome to Python world. Hello world, welcome to Python world.'
# 自己研究
count = 0
index = s2.find('world')
while index != -1:
    count += 1
    index = s2.find('world', index + 1)
print(count)

print(s2.count('world'))

print('-----------------------------')
# 大小寫切換
s3 = 'Hello world, welcome to Python world. Hello world, welcome to Python world.'
print(s3.capitalize())
print(s3.lower())
print(s3.upper())
print(s3.title())
print(s3.swapcase())

print('-----------------------------')
# 換字
print(s3.replace('Python', 'Java'))

print('-----------------------------')
# 刪除左右空白字元
s = '    Python    '
print(s.lstrip())
print(s.rstrip())
print(s.strip())

# 向左向右對齊
s = 'Python'
print(s.ljust(10))
print(s.rjust(10))
print(s.center(10))

