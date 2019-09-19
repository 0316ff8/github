# for包含式
# P136
list1 = [i * 3 for i in range(1, 11)]
print(list1)

set1 = {i * 3 for i in range(1, 11)}
print(set1)

dict1 = {i: i * 3 for i in range(1, 11)}
print(dict1)

tuple1 = (i * 3 for i in range(1, 11))
for val in tuple1:
    print(val)

list1 = [i for i in range(50) if i % 2 == 0]
print(list1)
list1 = [i for i in range(50) if i % 2 == 1]
print(list1)
list1 = [i for i in range(50) if i % 2] # 廣義的真為1, 所以會餘1(基數)
print(list1)
list1 = [i for i in range(50) if not(i % 2)]
print(list1)

#找出100以下的質數
