# 內建模組 random, statistics

# 載入模組
# import random

# 隨機選取
# import random
# 從列表中隨機選取1個資料
# random.choice([0,1,5,8])
# 從列表中隨機選取n個資料
# random.sample([0,1,5,8],n)

# 隨機選取
# import random
# 範例1
# data=random.choice([1,5,6,10,20])
# print(data)
# 範例2
# data=random.sample([1,5,6,10,20],3)
# print(data)

# 隨機調換順序(洗牌的概念)
# import random
# 將列表的資料「就地」隨機調換資料順序
# data=[0,1,5,8]
# random.shuffle(data)
# print(data)

# 隨機亂數
# import random
# 取得0.0~1.0之間的隨機亂數
# random.random()
# random.uniform(0.0,1.0)

# 取得隨機亂數
# 範例1
# import random
# data=random.random()    #取得 0~1 之間的隨機亂數
# print(data)
# 範例2
# import random
# data=random.uniform(60,100)    #取得 60~100 之間的隨機亂數
# print(data)

# 常態分配亂數
# import random
# 取得平均數100、標準差10的常態分配亂數
# random.normalvariate(100,10)

# 取得常態分配亂數
# 範例1
# 平均數100,標準差10,得到的資料【多數】在90到110之間
# import random
# data=random.normalvariate(100,10)
# print(data)
# 範例2
# 平均數0,標準差5,得到的資料【多數】在-5到5之間
# import random
# data=random.normalvariate(0,5)
# print(data)

#----------------------------------------------------------
# 統計模組

# 計算平均數
# import statistics
# 計算列表中數字的平均數
# statistics.mean([1,4,6,9])

# 範例1
# import statistics as stat
# data=stat.mean([1,4,5,8])
# print(data)

# 計算中位數
# import statistics
# 計算列表中數字的中位數
# statistics.median([1,4,6,9])
# 解法: 由小排到大，若列表數為單數取中間那個數值，若列表數為雙數將中間兩個數字相加/2

# 範例2
# import statistics as stat
# data=stat.median([1,2,3,4,6,6,8,100])   #(4+6)/2
# print(data)

#計算標準差
# import statistics
# 計算列表中數字標準差
# statistics.stdev([1,4,6,9])

#範例3
import statistics as stat
data=stat.stdev([1,2,3,4,5,8,10])
print(data)


# 平均數、中位數、標準差、常態分配
