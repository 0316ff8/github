# while迴圈

n = 1
total = 0
while n <= 10:
    total += n
    n += 1
print('total:',total)
print('n:', n)


n = 10
total = 0
while n >= 1:
    total += n
    n -= 1
print('total:',total) # 10加到1
print('n:', n)

# for in range()迴圈

total = 0
for n in range(1, 11, 1):
    total += n
print('total:',total)
print('n:', n)

total = 0
for n in range(1, 11):
    total += n
print('total:',total)
print('n:', n)

total = 0
for n in range(10, 0, -1):
    total += n
print('total:',total) # 10加到1
print('n:', n)

total = 0
for n in range(1, 101):
    total += n
print('total:',total)
print('n:', n)

total = 0
for n in range(2, 11, 2):
    total += n
print('total:',total) # 偶數相加
print('n:', n)

total = 0
for n in range(1, 11, 2):
    total += n
print('total:',total) # 基數相加
print('n:', n)