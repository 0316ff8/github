# 算術運算子
print(17/4) # 整除
print(17//4) # 商
print(17%4) # 餘數
print(2**4) # 次方

print('Leo' + ' Messi')
print(int('123') + 456)
print('123' + str(456))

print(-17//4) # 商(-4.25往負的方向走,取比較小的值)
print(-17%4) # 餘數

# 身分運算子
a = 10
b = a
print(id(a), id(b))
print(id(a) == id(b))
print(a is b)

a = a + 2
