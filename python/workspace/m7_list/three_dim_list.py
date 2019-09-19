# 三維陣列
# P118-P119
# list1 = [[[1, 2, 3], [4, 5, 6]], [[11, 22, 33], [44, 55, 66]]] # 2 * 2 * 3
# print(list1[0][0][0])
# print(list1[0][0][1])
# print(list1[0][0][2])
# print(list1[0][1][0])
# print(list1[0][1][1])
# print(list1[0][1][2])
# print(list1[1][0][0])
# print(list1[1][0][1])
# print(list1[1][0][2])
# print(list1[1][1][0])
# print(list1[1][1][1])
# print(list1[1][1][2])   # 索引值比陣列數各少1, 如: 2 * 2 * 3

# print(list1)
# print(list1[0]) # 第一層
# print(list1[1]) # 第二層

# print(list1[0][0]) # 第一層第一列
# print(list1[0][1]) # 第一層第二列
# print(list1[1][0]) # 第二層第一列
# print(list1[1][1]) # 第二層第二列

# print(len(list1))       # 層數
# print(len(list1[0]))    # 列數, 第一層有多少列
# print(len(list1[0][0])) # 行數, 第一層第一列有多少行
#
# print('-------------------------------------------')
#
# for i in range(len(list1)):
#     for j in range(len(list1[i])):
#         for k in range(len(list1[i][j])):
#             print(list1[i][j][k])       # 印出所有元素



# import random
# layer, row, col = eval(input('input layer, row and row:'))
# list1 = []
# for i in range(layer):
#     list1.append([])
#     for j in range(row):
#         list1.append([])
#         for k in range(col):
#             list1[i][j].append(random.randint(1, 100))
# print(list1)


list3 = [[[11, 32],[54, 25],[48, 63]],[[70, 20],[14,61],[73, 19]]]
# print(list3)
# print(len(list3))
# print(list3[0])
# print(list3[1])
#
# for i in range(len(list3)):
#     print(list3[i])
#
print(len(list3[0])) # 3
for i in range(len(list3)):  # 0,1
    for j in range(len(list3[i])): # 0,1,2
        print(list3[i][j])

print(len(list3[0][0])) # 2
for i in range(len(list3)):  # 0,1
    for j in range(len(list3[i])): # 0,1,2
        for k in range(len(list3[i][j])): # 0,1
            print('%-3d' % list3[i][j][k], end=',') #列印所有元素, 向左靠齊3個字元
            print() # 每列印一個元素空一行