#while迴圈(後面放布林值，若為True做迴圈)

#不要執行(無限迴圈)
#n=1
#while True:
#    print(n)
#    n+=1

# n=1
# while n<=3: #當n小於等於3為True，繼續跑程式；n大於4停止迴圈
#    print(n)
#    n+=1

# 1+2+3+....10
# n=1
# sum=0   #記錄累加的結果
# while n<=10:
#    sum+=n  #sum=sum+n
#    n+=1    #n=n+1
#    print(sum) #放裡面會顯示每次迴圈sum結果
# print(sum)  #與while對齊只印最後的sum結果

# sum=0+1=1,n=1+1=2
# sum=1+2=3,n=2+1=3
# sum=3+3=6,n=3+1=4
# sum=6+4=10,n=4+1=5
# sum=10+5=15,n=5+1=6
# sum=15+6=21,n=6+1=7
# sum=21+7=28,n=7+1=8
# sum=28+8=36,n=8+1=9
# sum=36+9=45,n=9+1=10
# sum=45+10=55,n=10+1=11

#for迴圈(for 變數 in 列表或字串，將列表或字串按順序放入x中)

# for x in [1,2,3]:
#    print(x)

# for x in "Messi":
#    print(x)

# for x in range(5):  #0,1,2,3,4
#    print(x)

#for x in range(5,10):  #從5到10不包含10
#    print(x)

#for迴圈做 1+2+3+...10

sum=0
for x in range(1,11):   #從1到11不包含11放入x
    sum+=x              #sum=sum+x，加到x=10的sum總合後列印出來
print(sum)