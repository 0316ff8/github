#break的簡易範例 (強制跳出 ❮整個❯ 迴圈)

# n=0
# while n<5:
#     if n==3:
#         break
#     print(n)           #印出迴圈中的n
#     n+=1
# print("最後的n:",n)    #印出迴圈結束後的n

#continue的簡易範例 (強制跳出 ❮本次❯ 迴圈，繼續進入下一圈)

# n=0
# for x in [0,1,2,3,4,5,6]:
#     if x%2==0:  #x是偶數
#         continue
#     print(x)
#     n+=1
# print("最後的n:",n)
#x為1時列印1，n=0+1=1；x為3時列印3，n=1+1=2

#else的簡易範例

# sum=0
# for n in range(11):
#     sum+=n
# else:
#     print(sum)  #印出 0+1+2+...+10的結果

#綜合範例: 找出整數平方根
#輸入9，得到3
#輸入11，得到【沒有】整數的平方根
# n=input("輸入一個正整數: ")
# n=int(n)    #轉換輸入成整數
# for i in range(n):  #i從 0 ~ n-1
#     if i*i==n:
#         print("整數平方根",i)
#         break   #用break強制結束迴圈時，不會執行else區塊
# else:
#     print("沒有整數平方根")
