# 集合的運算

# s1={1,2,3}
# print(3 in s1)  #核對資料是否在集合中，是為True，否為False

# s1={1,2,3}
# print(3 not in s1)  #核對資料是否不在集合中，是為True，否為False

# s1={1,2,3}
# s2={2,3,4}
# s3=s1&s2    #交集: 取兩個集合中，相同資料
# print(s3)
# s3=s1|s2    #聯集: 取兩個集合中的所有資料，但不重複取
# print(s3)
# s3=s1-s2    #差集: 從s1中，減去s2重複的部分
# print(s3)
# s3=s1^s2    #反交集: 取兩個集合中，不同疊部分
# print(s3)

# s=set("Messi")  #set(字串): 把字串中的字母拆解成集合，字母不重複
# print(s)

# s=set("Messi")  
# print("A" in s) #字串被拆解成集合之後用 in 來判斷 A字母是否在集合拆出來的字母中

#---------------------------------------------------------------------------

# 字典的運算: key-value配對

# dic={"Messi":"梅西","Jordan":"喬登"}
# print(dic["Messi"]) #輸入字典的key會取得相對應的value

# dic={"Messi":"梅西","Jordan":"喬登"}
# dic["Messi"]="球神梅西" #更改key資料為球神梅西
# print(dic["Messi"])

# dic={"Messi":"梅西","Jordan":"喬登"}
# print("Messi" in dic)   #判斷key是否存在

# dic={"Messi":"梅西","Jordan":"喬登"}
# print("Messi" not in dic)   #判斷key是否存在

# dic={"Messi":"梅西","Jordan":"喬登"}
# print(dic)
# del dic["Messi"]    #刪除字典中的健值對 (key-value pair)
# print(dic)

# dic={x:x*2 for x in [1,2,3]}    #從列表的資樂產生字典
# print(dic)

