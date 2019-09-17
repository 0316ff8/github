# 一維串列
list1 = ["Python", "C", "Java"]
print(list1)
print(list1[0])
print(list1[1])
print(list1[2])

for i in range(0, 3 ,1):
    print(list1[i])

for i in range(len(list1)):
    print(list1[i])

for val in list1:
    print(val)

print("---------------------------------------------")

list2 = [45, 23, 10, 99, 30]

def mysum(list1):
    total = 0
    for i in range(len(list1)):
        total += list1[i]
    return total
print(mysum(list2)) # 自訂函式mysum帶入串列算出總合
print(sum(list2))
print(max(list2))
print(min(list2))

print(30 in list1) # 確認30有沒有在list1中
print(30 in list2)

list3 = list1 + list2 #串列相加
print(list3)
print(list1 * 3)

# 將亂數1-100透過迴圈得知位置丟進空字串中
import random
list1 = []
for i in range(6):
    list1.append(random.randint(1,100))
print(list1)