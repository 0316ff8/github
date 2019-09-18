# 串列方法
# P108
list1 = []
list1.append(34)
list1.append(56)
print(list1)
list1.append(68) #新增68到最後面
print(list1)
list1.insert(1, 15) #新增15到索引1位置
print(list1)
val = list1.pop() #取最後位置後刪除
print(val)
print(list1)
val = list1.pop(1) # 取索引位置後刪除
print(val)
print(list1)

print("-------------------------------------------------------------")

list2 = [45, 23, 10, 77, 99, 30, 77, 11, 77]
print(list2.count(77)) #計數串列中有多少77
list2.remove(77) # 刪除串列中的值，若有多個就刪除第一個
print(list2)
print(list2.index(77)) #取得串列中77的索引
list3 = list2.copy() # 將串列list2複製到list3
list2.sort() # 由小排到大
print(list2)
list2.reverse() #反轉由小排到大變成由大排到小
print(list2)
print(list3)