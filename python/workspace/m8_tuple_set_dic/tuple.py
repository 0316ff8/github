# 數組
# P122, P125
tuple1 = ('Pythin', 'C', 'Java')

for i in range(len(tuple1)):
    print(tuple1[i])

for val in tuple1:
    print(val)

print(tuple1)

list1 = [1, 24, 57, 889, 4, 7]
tuple2 = tuple(list1)
print(tuple2)

str1 = 'Python'
tuple2 = tuple(str1)
print(tuple2)

tuple1 = (1, 2, 3, 4, 5)
tuple1 += (6,)      # 在tuple1後新增6
print(tuple1)
tuple1 += (7, 8)    # 在tuple1後新增7,8
print(tuple1)

del tuple1
#print(tuple1)
