#有序可變動列表 List

# grades=[70,80,60,90,100]
# print(grades)

# grades=[70,80,60,90,100]
# print(grades[0])    #列印grades中第0個位置中的資料

# grades=[70,80,60,90,100]
# grades[0]=66    #把66放到列表中的第1個位置
# print(grades)

# grades=[70,80,60,90,100]
# print(grades[1:4])  #列印grades中第1到第4個位置(不包含4)中的資料

# grades=[70,80,60,90,100]
# grades[1:4]=[]  #連續刪除列表中從第1到第4(不包含4)的資料
# print(grades)

# grades=[70,80,60,90,100]
# grades=grades+[77,99]   #列表串接，原來列表加上新的列表
# print(grades)

# grades=[70,80,60,90,100]
# lenght=len(grades)  #取得列表長度 len(列表資料)
# print(lenght)

# data=[[1,2,3],[4,5,6]]
# print(data[0][1])   #列印槽狀列表

# data=[[1,2,3],[4,5,6]]
# data[0][0:2]=[7,7,7]    #資料取代，將7,7,7取代1,2
# print(data[0])

#-----------------------------------------------------------

#有序不可變動列表 Tuple

# data=(1,2,3)
# print(data[0:2])

# data=(1,2,3)
# data[0]=5   #錯誤: Tuple的資樂不可以變動(所有操作都跟List一樣)
# print(data)