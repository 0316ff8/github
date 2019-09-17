# 二維串列
# P115-P117
# list1 = [[1, 2 ,3], [4, 5, 6]]
# print(list1[0][0])
# print(list1[0][1])
# print(list1[0][2])
# print(list1[1][0])
# print(list1[1][1])
# print(list1[1][2])
#
# print(list1)
# print(list1[0])
# print(list1[1])
#
# print(len(list1)) # 列長度
# print(len(list1[0])) # 行長度
#
# for i in range(len(list1)):
#     print(list1[i])
#
# total = 0
# for i in range(len(list1)):        # 列
#     for j in range(len(list1[i])): # 行
#         total += list1[i][j]
# print(total)


# total = 0
# row = 1   # 第二列
# for i in range(len(list1[row])):
#     # print(i)
#     print(list1[row][i])
#     total += list1[row][i]
# print(total)    # 第二列加總

# total = 0
# col = 1 #第二行
# for i in range(len(list1)):
#     total += list1[i][col]
# print(total)    #第二行加總

import random
row, col = eval(input('input a row and col:'))
list1 = []
for i in range(row):
    list1.append([])    # 在list1內新增[], 2列就兩個以此類推
    for j in range(col):
        list1[i].append(random.randint(1, 100))
print(list1)