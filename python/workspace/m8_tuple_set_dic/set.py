# 集合
# P126-P128
# tuple1 = (1,2,3,4,5,3,1)
# set1 = set(tuple1)
# print(set1)
#
# set1.add(6)
# print(set1)
# set1.remove(4)
# print(set1)

set1 = {1,2,3,5,8}
set2 = {1,3,5,7,9}
# 聯集: set1集合的所有元素, 加上set1與set2集合裡''沒重複"的元素
print(set1.union(set2))
print(set1 | set2)
# 交集: set1與set2共同的元素
print(set1.intersection(set2))
print(set1 & set2)
# 差集: set1減掉set2共同的元素剩下的元素
print(set1.difference(set2))
print(set1 - set2)
print(set2 - set1)
# 對稱差集: set1集合與set2集合沒有的元素
print(set1.symmetric_difference(set2))
print(set1 ^ set2)
# set3的所有集合是set1的部分集合, 則set3為子集合, set1為超集合
set3 = {1,3,5}
print(set3.issubset(set1))
print(set1.issuperset(set3))